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

    for x in range(6):
        out = d(className="android.widget.ListView",
                resourceId="android:id/list").swipe("up")
        if not out:
            print("Success: scroll down")
        wait(1)

    out = d(text="JPS").click()
    if not out:
        print("Success: press JPS")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait(10)

    out = d(className="android.widget.ListView",
            resourceId="android:id/list").swipe("up")
    if out:
        print("Success: scroll down")
    wait()

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

    out = d(className="android.widget.Button", text="⊕").click()
    if not out:
        print("Success: press plus")
    wait()

    out = d(className="android.view.View", text="5 And God called the light Day, and the darkness He called Night, "
                                                "and there was evening and there was morning, the first day.").click()
    if not out:
        print("Success: press 1.4")
    wait()

    out = d(className="android.widget.FrameLayout", index="2").click()
    if not out:
        print("Success: press 1.4")
    wait()

    out = d(text="JPS").click()
    if not out:
        print("Success: press JPS")
    wait()

    out = d(text="KJV").click()
    if not out:
        print("Success: press KJV")
    wait()

    out = d(className="android.view.View", text="5 And God called the light Day, and the darkness He called Night, "
                                                "and there was evening and there was morning, the first day.").click()
    if not out:
        print("Success: press 1.4")
    wait()

    out = d(text="JPS").click()
    if not out:
        print("Success: press JPS")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press More options")
    wait()

    out = d(text="Tabs").click()
    if not out:
        print("Success: press Tabs")
    wait()

    out = d(text="New Tab").click()
    if not out:
        print("Success: press new Tabs")
    wait()

    out = d(className="android.widget.Button", text="⊕").click()
    if not out:
        print("Success: press plus")
    wait()

    out = d(className="android.view.View", text="5 And God called the light Day, and the darkness He called Night, "
                                                "and there was evening and there was morning, the first day.").click()
    if not out:
        print("Success: press 1.4")
    wait()

    out = d(className="android.widget.FrameLayout", index="2").click()
    if not out:
        print("Success: press 1.4")
    wait()

    if not out:
        print("Success: press 1.4")
    wait()

    out = d(text="KJV").click()
    if not out:
        print("Success: press KJV")
    wait()

    out = d(text="AB").click()
    if not out:
        print("Success: press AB")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press More options")
    wait()

    out = d(text="Tabs").click()
    if not out:
        print("Success: press Tabs")
    wait()

    out = d(text="Switch to Tab …").click()
    if not out:
        print("Success: press Switch to Tab …")
    wait()

    out = d(text="Tab 1: Gen 1:1, Gen 1:1").click()
    if not out:
        print("Success: press Tab 1: Gen 1:1, Gen 1:1")
    wait()

    out = d(text="7225").click()
    if not out:
        print("Success: press 7225")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(className="android.view.View", text="5 And G-d called the light Day, and the darkness He called Night. "
                                                "And there was evening and there was morning, one day. ").click()
    if not out:
        print("Success: press 1.5")
    wait()

    out = d(text="Jewish Publication Society Old Testament", resourceId="net.bible.android.activity:id/documentTitle").long_click(duration=1)
    if out:
        print("Success: long click title")
    wait()

    out = d(text="JPS").long_click(duration=1)
    if out:
        print("Success: long click JPS")
    wait()

    out = d(resourceId="net.bible.android.activity:id/delete").click()
    if not out:
        print("Success: press delete")
    wait()

    out = d(text="OK").click()
    if not out:
        print("Success: press OK")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press Back")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press More options")
    wait()

    out = d(text="Tabs").click()
    if not out:
        print("Success: press Tabs")
    wait()

    out = d(text="Switch to Tab …").click()
    if not out:
        print("Success: press Switch to Tab …")
    wait()

    out = d(text="Tab 2: Gen 1:1, Gen 1:1").click()
    if not out:
        print("Success: press Tab 2: Gen 1:1, Gen 1:1")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
