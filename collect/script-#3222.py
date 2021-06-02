# bug reproduction script for bug #3222 of collect
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

    os.system("adb root && adb shell am start -n org.odk.collect.android/org.odk.collect.android.activities.MainMenuActivity")
    #d.app_start("org.odk.collect.android")
    #d.shell("am start -n org.odk.collect.android/org.odk.collect.android.activities.MainMenuActivity")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.odk.collect.android":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press more options")
    wait()

    out = d(text="General Settings").click()
    if not out:
        print("Success: press General Settings")
    wait()

    out = d(text="Form management").click()
    if not out:
        print("Success: press Form management")
    wait()

    out = d(text="Hide old form versions").click()
    if not out:
        print("Success: press Hide old form versions")
    wait()

    d.press("back")
    d.press("back")
    print("Success: doulbe back")

    out = d(text="Fill Blank Form").click()
    if not out:
        print("Success: press Fill Blank Form")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
