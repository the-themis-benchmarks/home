# bug reproduction script for bug #224 of MaterialFBook
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

    d.app_start("me.zeeroooo.materialfb")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "me.zeeroooo.materialfb":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    x, y = d(className="android.webkit.WebView").center()
    d.long_click(x, y-105, duration=1)
    print("Success: long click web page")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
