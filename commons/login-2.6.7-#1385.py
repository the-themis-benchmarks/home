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
    d.app_start("fr.free.nrw.commons.debug")
    wait()
    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "fr.free.nrw.commons.debug" and \
                ".WelcomeActivity" in current_app['activity']:
            break
        time.sleep(2)

    wait()
    d.swipe_ext("left")
    print("swipe left")
    wait()
    d.swipe_ext("left")
    print("swipe left")
    wait()
    d.swipe_ext("left")
    print("swipe left")
    wait()
    d.swipe_ext("left")
    print("swipe left")

    wait()
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons.debug:id/welcomeYesButton").click()
    if not out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons.debug:id/loginUsername").set_text("DroidFuzzing5")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.EditText", resourceId="fr.free.nrw.commons.debug:id/loginPassword").set_text("droid.fuzzing5")
    if out:
        print("SUCCESS")

    wait()
    out = d(className="android.widget.Button", resourceId="fr.free.nrw.commons.debug:id/loginButton").click()
    if not out:
        print("SUCCESS")

    wait()
    current_app = d.app_current()
    print(current_app['package'])
    print(current_app['activity'])
    if current_app['package'] == "fr.free.nrw.commons.debug" and \
            "contributions.ContributionsActivity" in current_app['activity']:
        print("****Login SUCCESS******")
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



