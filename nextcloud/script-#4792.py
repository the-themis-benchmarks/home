# bug reproduction script for bug #4792 of nextcloud
# this one requires a 1080*1920 screen
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

    d.app_start("com.nextcloud.client")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.nextcloud.client":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(className="android.widget.Button", resourceId="com.nextcloud.client:id/login").click()
    if not out:
        print("SUCCESS")

    wait()

    wait()
    out = d(className="android.widget.EditText", resourceId="com.nextcloud.client:id/hostUrlInput").set_text(
        "https://efss.qloud.my/")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.ImageButton", resourceId="com.nextcloud.client:id/testServerButton").click()
    if not out:
        print("SUCCESS")
    wait(20)

    d.click(537, 1188)

    wait()
    out = d(className="android.widget.EditText", resourceId="user").set_text("droidfuzzer@163.com")
    if out:
        print("SUCCESS")
    wait()

    out = d(className="android.widget.EditText", resourceId="password").set_text("droid.fuzzing")
    if out:
        print("SUCCESS")
    wait()

    out = d(text="Log in").click()
    if not out:
        print("SUCCESS")
    wait(5)

    out = d(text="Grant access").click()
    if not out:
        print("SUCCESS")
    wait(30)

    out = d(description="Open sidebar").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Auto upload").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(description="More options").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Set up a custom folder").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Remote folder").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(description="More options").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="New folder").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Name").set_text("A")
    if out:
        print("SUCCESS")
    wait()

    out = d(text="Create").click()
    if not out:
        print("SUCCESS")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
