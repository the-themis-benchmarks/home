# bug reproduction script for bug #10547 of wordpress
import os
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

def enAbleDontKeepA(d):
    d.press("home")
    wait()

    out = d(resourceId="com.android.launcher3:id/layout").child(index="1").child(index="2").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Search Apps…").set_text("Settings")
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="com.android.launcher3:id/icon", text="Settings").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(description="Search settings").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Search…").set_text("keep activities")
    if out:
        print("SUCCESS")
    wait()

    out = d(text="Don’t keep activities").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Don’t keep activities").click()
    if not out:
        print("SUCCESS")
    wait()

if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)

    enAbleDontKeepA(d)

    d.app_start("org.wordpress.android")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.wordpress.android":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/login_button").click()
    if not out:
        print("SUCCESS: press login button")

    wait()
    out = d(className="android.widget.TextView", resourceId="org.wordpress.android:id/login_site_button_text").click()
    if not out:
        print("SUCCESS: press login in via site address")

    wait()
    out = d(className="android.widget.EditText").set_text("testkkksite.wordpress.com")
    if out:
        print("SUCCESS: input site address")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/primary_button").click()
    if not out:
        print("SUCCESS: press next")

    wait()
    out = d(className="android.widget.EditText", resourceId="org.wordpress.android:id/input", text="Username").set_text(
        "testkkksite")
    if out:
        print("SUCCESS: input user name")

    wait()
    d.press("back")

    wait()
    out = d(className="android.widget.EditText", resourceId="org.wordpress.android:id/input", text="Password").set_text(
        "W11j141993")
    if out:
        print("SUCCESS: input password")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/primary_button").click()
    if not out:
        print("SUCCESS: press next")

    wait(5)

    out = d(text="CONTINUE").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/quick_action_buttons_container").child(index="2").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="DRAFTS").click()
    if not out:
        print("SUCCESS")
    wait(10)

    out = d(text="Edit").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(description="More options").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Preview").click()
    if not out:
        print("SUCCESS")
    wait(10)

    out = d(description="Navigate up").click()
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
