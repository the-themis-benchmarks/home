# bug reproduction script for bug #4881 of firefoxlite
# this one requires a 1080*1920 screen.
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

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(resourceId="org.mozilla.rocket.debug.ting:id/bottom_bar_home").click()
    if not out:
        print("Success: press shop")
    wait()

    out = d(text="Enter a product name").set_text("desk")
    if out:
        print("Success: enter desk")
    wait()

    out = d(text="desk", resourceId="org.mozilla.rocket.debug.ting:id/suggestion_item").click()
    if not out:
        print("Success: press desk")
    wait(15)

    d.click(760, 544)
    print("Success: press Videos")
    wait(10)

    out = d(className="android.webkit.WebView").swipe("up")
    if out:
        print("Success: scroll down")
    wait()

    d.click(493, 1597)
    print("Success: press Video")
    wait(30)

    d.click(549, 608)
    print("Success: press Video")
    wait(5)

    d.click(1020, 875)
    print("Success: press Video")
    wait(1)

    d.click(1020, 875)
    print("Success: press Video")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
