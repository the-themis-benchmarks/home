# bug reproduction script for bug #118 of ActivityDiary
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
    d.app_start("de.rampro.activitydiary.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "de.rampro.activitydiary.debug":
            break
        time.sleep(2)
    wait()

    # click the Sleeping activity
    out = d(className="android.widget.TextView", text="Sleeping").click()
    if not out:
        print("Success: press Sleeping activity")
    wait()

    # click the Sleeping activity
    out = d(className="android.widget.ImageButton", resourceId="de.rampro.activitydiary.debug:id/fab_attach_picture").click()
    if not out:
            print("Success: press Camera")
    wait()

    # click camera button
    out = d(className="android.widget.ImageView",
            resourceId="com.android.camera2:id/shutter_button").click()
    if not out:
        print("Success: press taking picture")
    wait()

    # click confirm
    out = d(className="android.widget.ImageButton",
            resourceId="com.android.camera2:id/done_button").click()
    if not out:
        print("Success: press picture confirmation")
    wait()

    # click the Cinema activity
    out = d(className="android.widget.TextView", text="Cinema").click()
    if not out:
        print("Success: press Cinema activity")
    wait()

    # click the Navigation
    out = d(className="android.widget.ImageButton", description="Open Navigation").click()
    if not out:
        print("Success: press Navigation")
    wait()

    # click the Diary
    out = d(className="android.widget.CheckedTextView", text="Diary").click()
    if not out:
        print("Success: press Diary")
    wait()

    # long click the image
    out = d(className="android.widget.ImageView",
            resourceId="de.rampro.activitydiary.debug:id/picture").long_click()
    if out:
        print("Success: long click the image")
    wait()

    # click the Okay
    out = d(className="android.widget.Button",
            text="OK").click()
    if not out:
        print("Success: long click the ok")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
