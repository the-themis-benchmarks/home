# bug reproduction script for bug #116 of APhotoManager
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

    d.app_start("de.k3b.android.androFotoFinder")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "de.k3b.android.androFotoFinder":
            break
        time.sleep(2)
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press more options")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: press Settings")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
