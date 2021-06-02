# bug reproduction script for bug #745 of Omni-Notes
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

    d.app_start("it.feio.android.omninotes")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "it.feio.android.omninotes":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(resourceId="it.feio.android.omninotes:id/fab_expand_menu_button").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="it.feio.android.omninotes:id/fab_note").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Content").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="it.feio.android.omninotes:id/menu_attachment").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Camera").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="com.android.camera2:id/shutter_button").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="com.android.camera2:id/done_button").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="it.feio.android.omninotes:id/root").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="it.feio.android.omninotes:id/gridview_item_picture").click()
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
