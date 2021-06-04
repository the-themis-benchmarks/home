# bug reproduction script for bug #3244 of commons
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

    d.app_start("fr.free.nrw.commons")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "fr.free.nrw.commons":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    d.swipe_ext("left")
    print("swipe left")
    wait()
    d.swipe_ext("left")
    print("swipe left")
    wait()
    d.swipe_ext("left")
    print("swipe left")
    wait()
    d.swipe_ext("left")
    print("swipe left")

    wait()
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons:id/finishTutorialButton").click()
    if not out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons:id/login_username").set_text(
        "DroidFuzzing5")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons:id/login_password").set_text(
        "droid.fuzzing5")
    if out:
        print("SUCCESS")

    wait()
    d.press("back")

    wait()
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons:id/login_button").click()
    if not out:
        print("SUCCESS")
    wait(15)

    out = d(text="NEARBY").click()
    if not out:
        print("Success: press NEARBY")
    wait()

    out = d(resourceId="fr.free.nrw.commons:id/list_sheet").click()
    if not out:
        print("Success: press display list")
    wait()

    out = d(text="Googleplex").click()
    if not out:
        print("Success: press Googleplex")
    wait()

    out = d(resourceId="fr.free.nrw.commons:id/cameraButton").click()
    if not out:
        print("Success: press Camera")
    wait()

    out = d(resourceId="com.android.camera2:id/shutter_button").click()
    if not out:
        print("Success: press Camera")
    wait()

    out = d(resourceId="com.android.camera2:id/done_button").click()
    if not out:
        print("Success: press Camera")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
