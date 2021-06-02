# bug reproduction script for bug #6145 of ankidroid
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

    d.app_start("com.ichi2.anki")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.ichi2.anki":
            break
        time.sleep(2)
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: press settings")
    wait()

    out = d(text="AnkiDroid").click()
    if not out:
        print("Success: press AnkiDroid")
    wait()

    out = d(className="android.widget.ListView").swipe("up", steps=10)
    if not out:
        print("Success: scroll down")
    wait(1)

    out = d(text="Language").click()
    if not out:
        print("Success: press Language")
    wait()

    out = d(text="Chinese (China)").click()
    if not out:
        print("Success: press Chinese (China)")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: press settings")
    wait()

    out = d(text="高级设置").click()
    if not out:
        print("Success: press 高级设置")
    wait()

    for x in range(6):
        out = d(className="android.widget.ListView").swipe("up", steps=10)
        if not out:
            print("Success: scroll down")
        wait(1)

    out = d(text="实验性 V2 调度器").click()
    if not out:
        print("Success: press 实验性 V2 调度器")
    wait()

    out = d(text="确定").click()
    if not out:
        print("Success: press 确定")
    wait()

    out = d(description="转到上一层级").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(description="转到上一层级").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press more options")
    wait()

    out = d(text="Export collection").click()
    if not out:
        print("Success: press Export collection")
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
