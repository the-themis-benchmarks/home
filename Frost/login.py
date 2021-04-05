# login script
import sys
import time

import uiautomator2 as u2

if __name__ == '__main__':
    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    d.WAIT_FOR_DEVICE_TIMEOUT = 70
    d.app_start("com.pitchedapps.frost.debug")
    time.sleep(5)
    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.pitchedapps.frost.debug" and \
                current_app['activity'] == "com.pitchedapps.frost.activities.LoginActivity":
            break
        time.sleep(2)
    time.sleep(5)
    out = d(className="android.widget.EditText", resourceId="m_login_email").set_text("droid_fuzzing@163.com")
    if out:
        print("SUCCESS")
    time.sleep(5)
    out = d(className="android.widget.EditText", resourceId="m_login_password").set_text("droid123&")
    if out:
        print("SUCCESS")
    time.sleep(5)
    out = d(className="android.widget.Button", text="Log In ").click()
    if out:
        print("SUCCESS")
    print("Login SUCCESS")
    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)



