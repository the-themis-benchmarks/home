# bug reproduction script for bug #2198 of attendee
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

    d.app_start("com.eventyay.attendee")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.eventyay.attendee":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(text="Skip").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Skip for now").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="com.eventyay.attendee:id/searchFragment").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Anything").click()
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
