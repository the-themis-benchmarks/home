# bug reproduction script for bug #703 of andbible
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    print("wait for " + str(seconds) + " second")
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
    wait()

    out = d(text="YES").click()
    if not out:
        print("Success: press YES")
    wait(30)

    out = d(text="KJV").click()
    if not out:
        print("Success: press KJV")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait(15)

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(text="I UNDERSTAND").click()
    if not out:
        print("Success: press I UNDERSTAND")
    wait()

    out = d(resourceId="3.20").long_click()
    if out:
        print("Success: long click 3.20")
    wait()

    out = d(resourceId="net.bible.android.activity:id/myNoteAddEdit").click()
    if not out:
        print("Success: press note")
    wait()

    out = d(resourceId="net.bible.android.activity:id/searchButton").click()
    if not out:
        print("Success: press search")
    wait()

    out = d(text="CREATE").click()
    if not out:
        print("Success: press create")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
