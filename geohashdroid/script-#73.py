# bug reproduction script for bug #73 of geohashdroid
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

    d.app_start("net.exclaimindustries.geohashdroid")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "net.exclaimindustries.geohashdroid":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(text="Cool").click()
    if not out:
        print("Success: press Cool")
    wait()

    out = d(text="GRATICULE").click()
    if not out:
        print("Success: press GRATICULE")
    wait()

    out = d(text="Globalhash!").click()
    if not out:
        print("Success: press Globalhash!")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
