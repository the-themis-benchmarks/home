# bug reproduction script for bug #6530 of wordpress
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

    d.app_start("com.android.camera2")
    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.android.camera2":
            break
        # d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    for x in range(15):
        out = d(resourceId="com.android.camera2:id/shutter_button").click()
        if not out:
            print("SUCCESS")
        wait(3)


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

    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/login_button").click()
    if not out:
        print("SUCCESS: press login button")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/secondary_button").click()
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
    out = d(className="TextInputLayout", text="Username").child(className="android.widget.EditText").set_text(
        "testkkksite")
    if out:
        print("SUCCESS: input user name")

    wait()
    out = d(className="TextInputLayout", text="Password").child(className="android.widget.EditText").set_text(
        "W11j141993")
    if out:
        print("SUCCESS: input password")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/primary_button").click()
    if not out:
        print("SUCCESS: press next")
    wait(10)

    out = d(text="CONTINUE").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="TRY IT").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Blog Posts").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/fab_button").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Share your story here…").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/format_bar_button_media").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").child(index="0").long_click()
    if out:
        print("SUCCESS")
    wait()

    for x in range(2, 9):
        out = d(resourceId="org.wordpress.android:id/recycler").child(index=str(x)).long_click()
        if out:
            print("SUCCESS")
        wait()

    out = d(resourceId="org.wordpress.android:id/recycler").swipe("up")
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").child(index="6").long_click()
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").child(index="7").long_click()
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").child(index="8").long_click()
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").swipe("up")
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").child(index="6").long_click()
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").child(index="7").long_click()
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/recycler").child(index="8").long_click()
    if out:
        print("SUCCESS")
    wait()

    out = d(resourceId="org.wordpress.android:id/mnu_confirm_selection").click()
    if not out:
        print("SUCCESS")
    wait(1)

    out = d(text="TURN ON").click()
    if not out:
        print("SUCCESS")
    wait(1)

    out = d(description="Navigate up").click()
    if not out:
        print("SUCCESS")
    wait(1)

    out = d(resourceId="org.wordpress.android:id/btn_trash").click()
    if not out:
        print("SUCCESS")
    wait(1)

    out = d(text="DELETE").click()
    if not out:
        print("SUCCESS")
    wait(1)

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
