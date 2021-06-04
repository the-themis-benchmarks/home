# bug reproduction script for bug #637 of osmeditor
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

    d.app_start("de.blau.android")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "de.blau.android":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(text="OKAY").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/location_current").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="LOAD").click()
    if not out:
        print("SUCCESS")
    wait(10)

    out = d(resourceId="de.blau.android:id/menu_config").click()
    if not out:
        print("SUCCESS")
    wait()

    for x in range(2):
        out = d(resourceId="de.blau.android:id/list").swipe("up", steps=10)
        if out:
            print("SUCCESS")
        wait(1)

    out = d(text="Validator preferences").click()
    if not out:
        print("SUCCESS")
    wait()

    for x in range(6):
        out = d(resourceId="de.blau.android:id/listViewResurvey").child(index="0").child(index="0").child(text="amenity").click()
        if not out:
            print("SUCCESS")
        wait()

        out = d(text="DELETE").click()
        if not out:
            print("SUCCESS")
        wait()

    out = d(text="name").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="DELETE").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="opening_hours").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="DELETE").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="wheelchair").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="DELETE").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/listViewResurvey").child(index="0").child(index="0").child(
        text="shop").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/resurvey_value").set_text("*")
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="de.blau.android:id/display").set_text("0")
    if out:
        print("SUCCESS")
    wait()

    out = d(text="SAVE").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="DONE").click()
    if not out:
        print("SUCCESS")
    wait()

    d.press("back")
    print("SUCCESS")

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
