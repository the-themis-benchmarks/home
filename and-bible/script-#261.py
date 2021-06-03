# bug reproduction script for bug #261 of andbible
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
    d.app_start("net.bible.android.activity")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "net.bible.android.activity":
            break
        time.sleep(2)
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait(30)

    out = d(text="AB").click()
    if not out:
        print("Success: press AB")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait(10)

    out = d(text="Bible").click()
    if not out:
        print("Success: press Bible")
    wait()

    out = d(text="Book").click()
    if not out:
        print("Success: press Book")
    wait()

    out = d(text="BaptistConfession1646").click()
    if not out:
        print("Success: press BaptistConfession1646")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait(5)

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(className="android.widget.ImageButton", resourceId="net.bible.android.activity:id/homeButton").click()
    if not out:
        print("Success: press home")
    wait()

    out = d(text="Choose Document").click()
    if not out:
        print("Success: press Choose Document")
    wait()

    out = d(text="Bible").click()
    if not out:
        print("Success: press Bible")
    wait()

    out = d(text="Book").click()
    if not out:
        print("Success: press Book")
    wait()

    out = d(text="BaptistConfession1646").click()
    if not out:
        print("Success: press BaptistConfession1646")
    wait()

    out = d(text="Confession").click()
    if not out:
        print("Success: press Confession")
    wait()

    out = d(className="android.widget.ImageButton", resourceId="net.bible.android.activity:id/homeButton").click()
    if not out:
        print("Success: press home")
    wait()

    out = d(text="Find").click()
    if not out:
        print("Success: press Find")
    wait()

    out = d(text="CREATE").click()
    if not out:
        print("Success: press Find")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
