#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: dumpCoverage.sh <outdir>"
    exit
fi

AVD_SERIAL=$1
APP_PACKAGE_NAME=$2
OUTPUT_DIR=$3

#for i in `seq 1 12`;
i=0
while true
do
  i=$((i+1))
  sleep 300 & # dump coverage for every 5 minutes
  wait
  adb -s $AVD_SERIAL shell am broadcast -a edu.gatech.m3.emma.COLLECT_COVERAGE
  adb -s $AVD_SERIAL pull /data/data/$APP_PACKAGE_NAME/files/coverage.ec $OUTPUT_DIR/coverage_$i.ec
  adb -s $AVD_SERIAL shell rm /data/data/$APP_PACKAGE_NAME/files/coverage.ec
done