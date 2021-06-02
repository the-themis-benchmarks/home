#!/bin/bash


APK_FILE=$1 # e.g., xx.apk
AVD_SERIAL=$2 # e.g., emulator-5554
AVD_NAME=$3 # e.g., base
OUTPUT_DIR=`realpath $4`
TEST_TIME=$5 # e.g., 10s, 10m, 10h
HEADLESS=$6 # e.g., -no-window
LOGIN_SCRIPT=$7 # the script for app login via uiautomator2

COMBO_DIR=../tools/combodroid/combo-separate
CURRENT_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# wait for the target device
function wait_for_device(){
    avd_serial=$1
    timeout 5s adb -s $avd_serial wait-for-device
    OUT=`adb -s $avd_serial shell getprop init.svc.bootanim`
    i=0
    while [[ ${OUT:0:7}  != 'stopped' ]]; do
      echo "   Waiting for emulator (${avd_serial}) to fully boot (#${i} times) ..."
      sleep 5
      i=$(expr $i + 1)
      if [[ $i == 10 ]]
      then
            echo "Cannot connect to the device: (${avd_serial}) after (#${i} times)..."
            break
      fi
      OUT=`adb -s $avd_serial shell getprop init.svc.bootanim`
    done
}

RETRY_TIMES=5
for i in $(seq 1 $RETRY_TIMES);
do
    echo "try to start the emulator (${AVD_SERIAL})..."
    sleep 5
    # start the emulator
    avd_port=${AVD_SERIAL:9:13}
    emulator -port $avd_port -avd $AVD_NAME -read-only $HEADLESS &
    sleep 5
    # wait for the emulator
    wait_for_device $AVD_SERIAL

    # check whether the emualtor is online
    OUT=`adb -s $avd_serial shell getprop init.svc.bootanim`
    if [[ ${OUT:0:7}  != 'stopped' ]]
    then
        adb -s $avd_serial emu kill
        echo "try to restart the emulator (${AVD_SERIAL})..."
        if [[ $i == RETRY_TIMES ]]
        then
            echo "we give up the emulator (${AVD_SERIAL})..."
            exit
        fi
    else
        break
    fi
done

echo "  emulator (${AVD_SERIAL}) is booted!"
adb -s ${AVD_SERIAL} root

current_date_time="`date "+%Y-%m-%d-%H-%M-%S"`"
apk_file_name=`basename $APK_FILE`
result_dir=$OUTPUT_DIR/$apk_file_name.combodroid.result.$AVD_SERIAL.$AVD_NAME\#$current_date_time
mkdir -p $result_dir
echo "** CREATING RESULT DIR (${AVD_SERIAL}): " $result_dir

# get app package
app_package_name=`aapt dump badging $APK_FILE | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g`
echo "** PROCESSING APP (${AVD_SERIAL}): " $app_package_name

### create config file before running combodroid
config_file=$COMBO_DIR/"Config_"${apk_file_name%.apk}-${AVD_SERIAL}".txt"
rm -rf $config_file
touch $config_file
echo "subject-dir = subjects" >> $config_file
unique_apk_file_name=${apk_file_name%.*}-$AVD_SERIAL".apk"
mkdir -p $COMBO_DIR/subjects
cp $APK_FILE $COMBO_DIR/subjects/$unique_apk_file_name
echo "apk-name = ${unique_apk_file_name}" >> $config_file
echo "instrument-output-dir = temp" >> $config_file
android_home=`printenv ANDROID_HOME`
echo "androidSDK-dir = ${android_home}" >> $config_file
echo "android-platform-version = 30" >> $config_file
echo "android-buildtool-version = 30.0.3" >> $config_file
real_path_of_combo=`realpath $COMBO_DIR`
echo "keystore-path = ${real_path_of_combo}/testKeyStore.jks" >> $config_file
echo "key-alias = combodroid" >> $config_file
echo "key-password = combodroid" >> $config_file
echo "package-name = ${app_package_name}" >> $config_file
echo "ComboDroid-type = alpha" >> $config_file
echo "trace-directory = traces" >> $config_file
echo "running-minutes = 360" >> $config_file
echo "modeling-minutes = 180" >> $config_file
port=${AVD_SERIAL##*-}
echo "serial = ${port}" >> $config_file
### end

config_file_name=`basename $config_file`


sleep 2
# login if necessary
if [[ $LOGIN_SCRIPT != "" ]]
then

    # instrumented the app
    cd $COMBO_DIR
    adb -s ${AVD_SERIAL} uninstall ${app_package_name}
    ./ComboDroid_instrument.sh $config_file_name >> $result_dir/combodroid.log 2>&1

    cd $CURRENT_SCRIPT_DIR
    echo "** APP LOGIN (${AVD_SERIAL})"
    python3 $LOGIN_SCRIPT ${AVD_SERIAL} combo 2>&1 | tee $result_dir/login.log

    sleep 10

    adb -s $avd_serial emu kill
    exit

else
    # do nothing
    echo "start to test"
    echo " *** Login SUCCESS ****" >> $result_dir/login.log
fi
sleep 2


# start logcat
echo "** START LOGCAT (${AVD_SERIAL}) "
adb -s $AVD_SERIAL logcat -c
adb -s $AVD_SERIAL logcat AndroidRuntime:E CrashAnrDetector:D System.err:W CustomActivityOnCrash:E ACRA:E WordPress-EDITOR:E *:F *:S > $result_dir/logcat.log &

# start coverage dumping
echo "** START COVERAGE (${AVD_SERIAL}) "
cd $CURRENT_SCRIPT_DIR
bash dump_coverage.sh $AVD_SERIAL $app_package_name $result_dir &

# run combodroid
echo "** RUN COMBODROID (${AVD_SERIAL})"
adb -s $AVD_SERIAL shell date "+%Y-%m-%d-%H-%M-%S" >> $result_dir/combo_testing_time_on_emulator.txt
# jump to combodroid's dir
cd $COMBO_DIR
timeout $TEST_TIME ./ComboDroid_execute.sh $config_file_name 2>&1 | tee $result_dir/combodroid.log 
adb -s $AVD_SERIAL shell date "+%Y-%m-%d-%H-%M-%S" >> $result_dir/combo_testing_time_on_emulator.txt

# stop coverage dumping
echo "** STOP COVERAGE (${AVD_SERIAL})"
kill `ps aux | grep "dump_coverage.sh ${AVD_SERIAL}" | grep -v grep |  awk '{print $2}'`

# stop logcat
echo "** STOP LOGCAT (${AVD_SERIAL})"
kill `ps aux | grep "${AVD_SERIAL} logcat" | grep -v grep | awk '{print $2}'`

# stop and kill the emulator
sleep 5
adb -s $AVD_SERIAL emu kill

echo "@@@@@@ Finish (${AVD_SERIAL}): " $app_package_name "@@@@@@@"
