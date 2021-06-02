# bug reproduction script for bug #4942 of firefoxlite
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

    os.system(
        "adb root && adb shell am start -n org.mozilla.rocket.debug.ting/org.mozilla.focus.activity.MainActivity")
   # d.app_start("org.mozilla.rocket.debug.ting")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.mozilla.rocket.debug.ting":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    d.shell("settings put global always_finish_activities 1")

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(text="YouTube").click()
    if not out:
        print("Success: press YouTube")
    wait(10)

    d.press("home")
    print("Success: press home")

    d.press("recent")
    print("Success: press recent")

    out = d(text="Firefox Lite Dev").click()
    if not out:
        print("Success: press Firefox Lite Dev")
    wait()

    out = d(resourceId="org.mozilla.rocket.debug.ting:id/counter_box").click()
    if not out:
        print("Success: press Firefox Lite Dev")
    wait()

    d.shell("settings put global always_finish_activities 0")

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
