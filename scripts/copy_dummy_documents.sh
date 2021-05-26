#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Usage: copy_dummy_documents.sh avd_serial"
    exit
fi

AVD_SERIAL=$1

# copy pictures
adb -s $AVD_SERIAL push ../dummy_documents/Android_logo.jpg /sdcard/Pictures/
adb -s $AVD_SERIAL push ../dummy_documents/Android_robot.png /sdcard/Pictures/
adb -s $AVD_SERIAL push ../dummy_documents/droidbot_utg.png /sdcard/Pictures/

# copy musics
adb -s $AVD_SERIAL push ../dummy_documents/Heartbeat.mp3 /sdcard/Music/
adb -s $AVD_SERIAL push ../dummy_documents/intermission.mp3 /sdcard/Music/

# copy movies
adb -s $AVD_SERIAL push ../dummy_documents/sample_iPod.m4v /sdcard/Movies/
adb -s $AVD_SERIAL push ../dummy_documents/sample_mpeg4.mp4 /sdcard/Movies/
adb -s $AVD_SERIAL push ../dummy_documents/sample_sorenson.mov /sdcard/Movies/
adb -s $AVD_SERIAL push ../dummy_documents/sample.3gp /sdcard/Movies/

# copy docs
adb -s $AVD_SERIAL push ../dummy_documents/DroidBot_documentation.docx /sdcard/Download/
adb -s $AVD_SERIAL push ../dummy_documents/DroidBot_documentation.pdf /sdcard/Download/
adb -s $AVD_SERIAL push ../dummy_documents/password.txt /sdcard/Download/
adb -s $AVD_SERIAL push ../dummy_documents/sample_3GPP.3gp.zip /sdcard/Download/