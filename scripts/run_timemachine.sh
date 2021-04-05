#!/bin/bash

# When fuzzing via TimeMachine, the aut's classfiles are stored under the same directory of the apk

APK_FILE=$1 # e.g., xx.apk
AVD_SERIAL=$2 # e.g., emulator-5554
AVD_NAME=$3 # e.g., base
OUTPUT_DIR=`realpath $4`
TEST_TIME=$5 # e.g., 10s, 10m, 10h
HEADLESS=$6 # e.g., -no-window
LOGIN_SCRIPT=$7 # the script for app login via uiautomator2
ADB_PORT=$8

echo "----"
echo "ADB_PORT: ${ADB_PORT}"
echo "----"

# check machine name to enable run TimeMachine on ETH/machines
host_machine_name=`hostname`
TIMEMACHINE_TOOL=../tools/TimeMachine

headless_option=1
if [[ ${HEADLESS} == "-no-window" ]]
then
    headless_option=1
else
    headless_option=0
fi

current_date_time="`date "+%Y-%m-%d-%H-%M-%S"`"
apk_file_name=`basename $APK_FILE`
apk_file_path=`realpath $APK_FILE`
apk_dir_path=`dirname $apk_file_path`
result_dir=$OUTPUT_DIR/$apk_file_name.timemachine.result.$AVD_SERIAL\#$current_date_time
mkdir -p $result_dir
echo "** CREATING RESULT DIR (${AVD_SERIAL}): " $result_dir

# get app package
app_package_name=`aapt dump badging $APK_FILE | grep package | awk '{print $2}' | sed s/name=//g | sed s/\'//g`
echo "** PROCESSING APP (${AVD_SERIAL}): " $app_package_name

# run TimeMachine
# jump into TimeMachine's exec folder
cd ${TIMEMACHINE_TOOL}/fuzzingandroid
echo "** RUN TIMEMACHINE "
echo "`date "+%Y-%m-%d-%H:%M:%S"`" >> $result_dir/timemachine_testing_time.txt
cmd="./exec-single-app.bash $apk_dir_path 0 droidtest/timemachine:1.0 $TEST_TIME $result_dir $apk_file_path $ADB_PORT $LOGIN_SCRIPT"
echo $cmd
timeout 6.5h ./exec-single-app.bash $apk_dir_path 0 ${headless_option} droidtest/timemachine:1.0 $TEST_TIME $result_dir $apk_file_path $ADB_PORT $LOGIN_SCRIPT
echo "`date "+%Y-%m-%d-%H:%M:%S"`" >> $result_dir/timemachine_testing_time.txt

echo "@@@@@@ Finish (${AVD_SERIAL}): " $app_package_name "@@@@@@@"
