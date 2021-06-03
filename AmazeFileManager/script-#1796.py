# bug reproduction script for bug #1796 of AFM
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
    d.app_start("com.amaze.filemanager")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.amaze.filemanager":
            break
        time.sleep(2)
    wait()

    out = d(className="android.widget.TextView", text="Alarms").click()
    if not out:
        print("Success: press Alarms")
    wait()

    out = d(className="android.widget.ImageButton", resourceId="com.amaze.filemanager:id/fab_expand_menu_button").click()
    if not out:
        print("Success: press plus")
    wait()

    out = d(className="android.widget.ImageButton", resourceId="com.amaze.filemanager:id/menu_new_folder").click()
    if not out:
        print("Success: press Folder")
    wait()

    out = d(className="android.widget.EditText", resourceId="com.amaze.filemanager:id/singleedittext_input").set_text(text="test")
    if out:
        print("Success: set folder name")
    wait()

    out = d(className="android.widget.TextView", text="CREATE").click()
    if not out:
        print("Success: press CREATE")
    wait()

    out = d(className="android.widget.TextView", text="test").long_click()
    if out:
        print("Success: long click test")
    wait()

    out = d(className="android.widget.TextView", resourceId="com.amaze.filemanager:id/cut").click()
    if not out:
        print("Success: press cut")
    wait()

    out = d(className="android.widget.TextView", text="test").click()
    if not out:
        print("Success: press test")
    wait()

    out = d(className="android.widget.TextView", resourceId="com.amaze.filemanager:id/paste").click()
    if not out:
        print("Success: press paste")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
