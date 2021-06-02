# bug reproduction script for bug #1323 of Frost
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

    d.app_start("com.pitchedapps.frost.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.pitchedapps.frost.debug":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(className="android.widget.EditText", resourceId="m_login_email").set_text("droidfuzzer@163.com")
    if out:
        print("SUCCESS")
    wait()

    out = d(className="android.widget.EditText", resourceId="m_login_password").set_text("droid.fuzzing")
    if out:
        print("SUCCESS")
    wait()

    out = d(className="android.widget.Button", text="Log In ").click()
    if out:
        print("SUCCESS")
    wait(30)

    out = d(text="SKIP").click()
    if out:
        print("SUCCESS: press SKIP")
    wait()

    out = d(className="androidx.appcompat.app.ActionBar$Tab", index="3").click()
    if not out:
        print("Success: press menu")
    wait()

    d.press("home")
    print("Success: press home")
    wait()

    d.shell("svc data disable")

    print("Success: disable network")
    wait()

    d.app_stop("com.pitchedapps.frost.debug")
    print("stop app")
    wait()

    d.app_start("com.pitchedapps.frost.debug")
    print("re-start app")
    wait()

    d.shell("svc data enable")


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
