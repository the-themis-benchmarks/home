# bug reproduction script for bug #1391 of commons
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

    d.app_start("fr.free.nrw.commons.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "fr.free.nrw.commons.debug":
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
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons.debug:id/welcomeYesButton").click()
    if not out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons.debug:id/loginUsername").set_text(
        "DroidFuzzing5")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons.debug:id/loginPassword").set_text(
        "droid.fuzzing5")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons.debug:id/loginButton").click()
    if not out:
        print("SUCCESS")
    wait(5)

    out = d(description="Open").click()
    if not out:
        print("Success: press Open")
    wait()

    out = d(text="Nearby").click()
    if not out:
        print("Success: press Nearby")
    wait(15)

    out = d(resourceId="fr.free.nrw.commons.debug:id/fab_recenter").click()
    if not out:
        print("SUCCESS: press center")
    wait()

    d.press(697, 1085)

    out = d(resourceId="fr.free.nrw.commons.debug:id/bottom_sheet_details").swipe("up")
    if not out:
        print("SUCCESS: swip up")
    wait()

    out = d(description="Open").click()
    if not out:
        print("Success: press Open")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: press Settings")
    wait()

    out = d(text="Night mode").click()
    if not out:
        print("Success: press Night mode")
    wait()

    out = d(description="Open").click()
    if not out:
        print("Success: press Open")
    wait()

    out = d(text="Nearby").click()
    if not out:
        print("Success: press Nearby")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
