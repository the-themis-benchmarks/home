# bug reproduction script for bug #4451of ankidroid
import sys
import time

import uiautomator2 as u2

# Among Android 6.0, 7.1 and 10.0, this bug is only reproducible on Android 6.0 and 7.1.

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)


    d.app_start("net.gsantner.markor")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "net.gsantner.markor":
            break
        time.sleep(2)
    wait()

    out = d(resourceId="net.gsantner.markor:id/action_search").click()
    if not out:
        print("Success: click search")
    wait()

    out = d.set_orientation('l')
    if not out:
        print("Success: left screen")
    wait()

    out = d.set_orientation("n")
    if not out:
        print("Success: natural screen")
    wait()

    out = d(resourceId="android:id/button1").click()
    if not out:
        print("Success: click Ok")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
