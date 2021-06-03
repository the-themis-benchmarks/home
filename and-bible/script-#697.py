# bug reproduction script for bug #697 of andbible
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
    wait(10)

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(text="I UNDERSTAND").click()
    if not out:
        print("Success: press I UNDERSTAND")
    wait()

    for x in range(20):
        out = d(className="android.webkit.WebView").swipe("down", steps=10)
        if not out:
            print("Success: scroll down")
        wait(1)

    out = d(resourceId="1.1").long_click()
    if out:
        print("Success: long click 1.1")
    wait()

    out = d(resourceId="net.bible.android.activity:id/myNoteAddEdit").click()
    if not out:
        print("Success: press note")
    wait()

    out = d(className="android.widget.EditText").click()
    if not out:
        print("Success: press edit text")
    wait()

    out = d(className="android.widget.EditText").set_text("hello")
    if not out:
        print("Success: set note")
    wait()

    out = d.press("back")
    out = d.press("back")
    if not out:
        print("Success: double back")
    wait()

    out = d(text="pencil16x16").click()
    if not out:
        print("Success: press note")
    wait()

    out = d(className="android.widget.EditText").set_text("world")
    if not out:
        print("Success: set note")
    wait()

    out = d.press("back")
    if not out:
        print("Success: press back")
    wait()

    out = d(resourceId="net.bible.android.activity:id/homeButton").click()
    if not out:
        print("Success: press home")
    wait()

    out = d(text="My Notes").click()
    if not out:
        print("Success: press My Notes")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
