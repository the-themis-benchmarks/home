# bug reproduction script for bug #239 of sunflower
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

    d.app_start("com.google.samples.apps.sunflower")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.google.samples.apps.sunflower":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Plant list").click()
    if not out:
        print("SUCCESS")
    wait()

    x1, y1 = d(text="Beet").center()
    x2, y2 = d(text="Avocado").center()

    d(className="androidx.recyclerview.widget.RecyclerView").gesture((x1, y1), (x2, y2), (x1, y1), (x2, y2), steps=50)
    print("SUCCESS")

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
