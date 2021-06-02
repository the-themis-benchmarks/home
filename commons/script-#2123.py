# bug reproduction script for bug #2123 of commons
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
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons:id/welcomeYesButton").click()
    if not out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons:id/loginUsername").set_text(
        "DroidFuzzing2")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons:id/loginPassword").set_text(
        "droid.fuzzing2")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons:id/loginButton").click()
    if not out:
        print("SUCCESS")
    wait(10)

    out = d(description="Open").click()
    if not out:
        print("Success: press Open")
    wait()

    out = d(text="Explore").click()
    if not out:
        print("Success: press Explore")
    wait()

    out = d(resourceId="fr.free.nrw.commons:id/action_search").click()
    if not out:
        print("Success: press search")
    wait()

    out = d(text="Search Commons").set_text("apple")
    if out:
        print("Success: set search text")
    wait(5)

    out = d(resourceId="fr.free.nrw.commons:id/categoryImageView").click()
    if not out:
        print("Success: press the first pic")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
