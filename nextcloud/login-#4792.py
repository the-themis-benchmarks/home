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
    device_type = sys.argv[2]
    d = u2.connect(avd_serial)
    # d.WAIT_FOR_DEVICE_TIMEOUT = 70
    d.app_start("com.nextcloud.client")
    wait()
    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.nextcloud.client" and \
                ".onboarding.FirstRunActivity" in current_app['activity']:
            break
        time.sleep(2)

    wait()
    out = d(className="android.widget.Button", resourceId="com.nextcloud.client:id/login").click()
    if not out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="com.nextcloud.client:id/hostUrlInput").set_text(
        "https://shared02.opsone-cloud.ch/")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.ImageButton", resourceId="com.nextcloud.client:id/testServerButton").click()
    if not out:
        print("SUCCESS")

    wait()
    if device_type == "humandroid":
        out = d(className="android.widget.Button", text="Log in").click()
    elif device_type == "timemachine":
        out = d.click(500, 420)
    else:
        out = d.click(400, 600)
    if not out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="user").set_text("droid_fuzzing_3@163.com")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="password").set_text("droid.fuzzing")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.Button", resourceId="submit-form").click()
    if not out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.Button", resourceId="").click()
    if not out:
        print("SUCCESS")

    wait()
    current_app = d.app_current()
    print(current_app['package'])
    print(current_app['activity'])
    if (current_app['package'] == "com.nextcloud.client" and
        "ui.activity.FileDisplayActivity" in current_app['activity']) or \
            (current_app['package'] == "com.google.android.packageinstaller" and
             "permission.ui.GrantPermissionsActivity" in current_app['activity']):
        print("****Login SUCCESS****")
    else:
        print("Login Failed")

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
