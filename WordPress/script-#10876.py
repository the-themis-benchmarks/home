# bug reproduction script for bug #10876 of wordpress
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

    out = d(resourceId="org.wordpress.android:id/bottom_nav_new_post_button").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Share your story here…").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/format_bottom_bar_undo").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/format_bottom_bar_redo").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/format_bar_button_media_collapsed").click()
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
