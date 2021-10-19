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
    d = u2.connect(avd_serial)
    # d.WAIT_FOR_DEVICE_TIMEOUT = 70
    d.app_start("org.wordpress.android")
    wait()
    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.wordpress.android" and \
                "ui.accounts.LoginActivity" in current_app['activity']:
            break
        time.sleep(2)

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/continue_with_wpcom_button").click()
    if not out:
        print("SUCCESS: press login button")


    wait()
    d.xpath('//*[@resource-id="org.wordpress.android:id/input_layout"]/android.widget.FrameLayout[1]').click()
    out = d.send_keys("ecnutesterjojo@163.com", clear=True)
    if out:
        print("SUCCESS: input email address")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/login_continue_button").click()
    if not out:
        print("SUCCESS: press continue")


    wait()
    d.xpath('//*[@resource-id="org.wordpress.android:id/input_layout"]/android.widget.FrameLayout[1]').click()
    out = d.send_keys("Qm#ZZ^.8/9#K6&v", clear=True)
    if out:
        print("SUCCESS: input password")

    wait()
    out = d(className="android.widget.Button", resourceId="org.wordpress.android:id/bottom_button").click()
    if not out:
        print("SUCCESS: press continue")

    wait()
    current_app = d.app_current()
    print(current_app['package'])
    print(current_app['activity'])
    if current_app['package'] == "org.wordpress.android" and \
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
