# login script
import sys
import time

import uiautomator2 as u2


def wait(seconds=10):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':
    avd_serial = sys.argv[1]
    print(avd_serial)
    d = u2.connect_adb_wifi(avd_serial)
    # d.WAIT_FOR_DEVICE_TIMEOUT = 70
    wait()
    d.app_start("org.wordpress.android.prealpha")
    print("start the app")
    wait()
    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.wordpress.android.prealpha" and \
                "ui.accounts.LoginActivity" in current_app['activity']:
            break
        time.sleep(2)

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android.prealpha:id/login_button").click()
    if not out:
        print("SUCCESS: press login button")

    wait()
    out = d(className="android.widget.LinearLayout", resourceId="org.wordpress.android.prealpha:id/login_site_button").click()
    if not out:
        print("SUCCESS: press login in via site address")

    wait()
    out = d(className="android.widget.EditText").set_text("https://ecnutesterjojo.wordpress.com/")
    if out:
        print("SUCCESS: input site address")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android.prealpha:id/primary_button").click()
    if not out:
        print("SUCCESS: press next")

    wait()
    out = d(className="android.widget.EditText", resourceId="org.wordpress.android.prealpha:id/input", text="Username").set_text(
        "ecnutesterjojo@163.com")
    if out:
        print("SUCCESS: input user name")

    wait()
    out = d(className="android.widget.EditText", resourceId="org.wordpress.android.prealpha:id/input", text="Password").set_text("Qm#ZZ^.8/9#K6&v")
    if out:
        print("SUCCESS: input password")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android.prealpha:id/primary_button").click()
    if not out:
        print("SUCCESS: press next")

    wait()
    current_app = d.app_current()
    print(current_app['package'])
    print(current_app['activity'])
    if current_app['package'] == "org.wordpress.android.prealpha" and \
            "ui.accounts.LoginEpilogueActivity" in current_app['activity']:
        print("****Login SUCCESS*****")
    else:
        print("****Login Failed*****")

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
