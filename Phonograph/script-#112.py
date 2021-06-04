# bug reproduction script for bug #112 of Phonograph
# This one requires two songs in the music folder
import os
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    os.system("adb push music1.mp3 sdcard/Music")
    os.system("adb push music2.mp3 sdcard/Music")

    d.app_start("com.kabouzeid.gramophone.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.kabouzeid.gramophone.debug":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(text="GET STARTED").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="SHUFFLE ALL").click()
    if not out:
        print("SUCCESS")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
