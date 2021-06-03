# bug reproduction script for bug #480 of andbible
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
    wait(30)

    out = d(text="AB").click()
    if not out:
        print("Success: press AB")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait(10)

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(description="Menu").click()
    if not out:
        print("Success: press Menu")
    wait()

    out = d(text="Manage Bookmark Labels").click()
    if not out:
        print("Success: press Manage Bookmark Labels")
    wait()

    out = d(text="NEW LABEL").click()
    if not out:
        print("Success: press NEW LABEL")
    wait()

    out = d(text="Name").set_text("first")
    if out:
        print("Success: set name first")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(text="NEW LABEL").click()
    if not out:
        print("Success: press NEW LABEL")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(className="android.widget.LinearLayout", index="1").child(resourceId="net.bible.android.activity:id/deleteLabel").click()
    if not out:
        print("Success: press delete")
    wait()

    out = d(resourceId="net.bible.android.activity:id/editLabel").click()
    if not out:
        print("Success: press NEW LABEL")
    wait()

    out = d(text="Name").set_text("second")
    if out:
        print("Success: set name second")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
