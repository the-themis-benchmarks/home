# bug reproduction script for bug #4942 of firefoxlite
import os
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

def enAbleDontKeepA(d):
    d.press("home")
    wait()

    out = d(resourceId="com.android.launcher3:id/layout").child(index="1").child(index="2").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Search Apps…").set_text("Settings")
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="com.android.launcher3:id/icon", text="Settings").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(description="Search settings").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Search…").set_text("keep activities")
    if out:
        print("SUCCESS")
    wait()

    out = d(text="Don’t keep activities").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Don’t keep activities").click()
    if not out:
        print("SUCCESS")
    wait()

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    enAbleDontKeepA(d)

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

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
