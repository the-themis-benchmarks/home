#!/bin/bash

APK_FILE=$1 # e.g., xx.apk
AVD_SERIAL=$2 # e.g., emulator-5554
AVD_NAME=$3 # e.g., base
OUTPUT_DIR=$4
TEST_TIME=$5 # e.g., 10s, 10m, 10h
HEADLESS=$6 # e.g., -no-window
LOGIN_SCRIPT=$7 # the script for app login via uiautomator2

STOAT_TOOL=../tool/Stoat/bin

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
avd_port=${AVD_SERIAL:9:13}
base_num=3554
stoat_port="$(($avd_port-$base_num))"
for i in $(seq 1 $RETRY_TIMES);
do
    echo "try to start the emulator (${AVD_SERIAL})..."
    sleep 5
    # start the emulator
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
result_dir=$OUTPUT_DIR/$apk_file_name.monkey.result.$AVD_SERIAL.$AVD_NAME\#$current_date_time
mkdir -p $result_dir
echo "** CREATING RESULT DIR (${AVD_SERIAL}): " $result_dir

# login if necessary
if [[ $LOGIN_SCRIPT != "" ]]
then
    echo "** APP LOGIN (${AVD_SERIAL})"

    # enable if use the login script
    # adb -s $AVD_SERIAL install -g $APK_FILE &> $result_dir/install.log
    # echo "** INSTALL APP (${AVD_SERIAL})"
    # python3 $LOGIN_SCRIPT ${AVD_SERIAL} 2>&1 | tee $result_dir/login.log

    # enable if use the snapshot (already login, do not need to install the app)
    echo " *** Login SUCCESS ****" >> $result_dir/login.log

else
    # install the app
    sleep 5 # wait for a few seconds before installation to avoid such error: "adb: connect error for write: closed"
    adb -s $AVD_SERIAL install -g $APK_FILE &> $result_dir/install.log
    echo "** INSTALL APP (${AVD_SERIAL})"
fi

sleep 10

# get app package
app_package_name=`aapt dump badging $APK_FILE | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g`
echo "** PROCESSING APP (${AVD_SERIAL}): " $app_package_name

# start logcat
echo "** START LOGCAT (${AVD_SERIAL}) "
adb -s $AVD_SERIAL logcat -c
adb -s $AVD_SERIAL logcat -G 10M
adb -s $AVD_SERIAL logcat AndroidRuntime:E CrashAnrDetector:D System.err:W CustomActivityOnCrash:E ACRA:E WordPress-EDITOR:E *:F *:S > $result_dir/logcat.log &

# start coverage dumping
#echo "** START COVERAGE (${AVD_SERIAL}) "
#bash dump_coverage.sh $AVD_SERIAL $app_package_name $result_dir &

# run Stoat
echo "** RUN STOAT (${AVD_SERIAL})"
cd $STOAT_TOOL
adb -s $AVD_SERIAL shell date "+%Y-%m-%d-%H:%M:%S" >> $result_dir/stoat_testing_time_on_emulator.txt
ruby run_stoat_testing.rb --app_dir $result_dir --apk_path $APK_FILE --avd_port $avd_port --stoat_port $stoat_port --model_time 1h --mcmc_time 5h --project_type gradle #2>&1 | tee $result_dir/stoat.log
adb -s $AVD_SERIAL shell date "+%Y-%m-%d-%H:%M:%S" >> $result_dir/stoat_testing_time_on_emulator.txt

# stop coverage dumping
#echo "** STOP COVERAGE (${AVD_SERIAL})"
#kill `ps aux | grep "dump_coverage.sh ${AVD_SERIAL}" | grep -v grep |  awk '{print $2}'`

# stop logcat
echo "** STOP LOGCAT (${AVD_SERIAL})"
kill `ps aux | grep "${AVD_SERIAL} logcat" | grep -v grep | awk '{print $2}'`

# stop and kill the emulator
sleep 5
adb -s $AVD_SERIAL emu kill

echo "@@@@@@ Finish (${AVD_SERIAL}): " $app_package_name "@@@@@@@"
