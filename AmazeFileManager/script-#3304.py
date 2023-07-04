# bug reproduction script for bug #1232 of AFM
import sys
import time

import uiautomator2 as u2


FILE_NAME = "www.google.com"

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

    # out = d(className="android.widget.TextView", text="Alarms").long_click()
    # if out:
    #     print("Success: long click Alarms")
    # wait()

    out = d(className="android.widget.ImageButton", resourceId="com.amaze.filemanager:id/fab_expand_menu_button").click()
    if not out:
        print("Success: click add")
    wait()

    out = d(className="android.widget.ImageButton", resourceId="com.amaze.filemanager:id/menu_new_file").click()
    if not out:
        print("Success: click  new file")
    wait()

    out = d(className="android.widget.EditText",resourceId="com.amaze.filemanager:id/singleedittext_input").set_text(text=FILE_NAME)
    if out:
        print("Success: set file name")
    wait()

    out = d(className="android.widget.TextView",resourceId="com.amaze.filemanager:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: click create")
    wait()

    out = d(className="android.widget.TextView", resourceId="com.amaze.filemanager:id/search").click()
    if not out:
        print("Success: click search")
    wait()

    out = d(className="android.widget.EditText", resourceId="com.amaze.filemanager:id/search_edit_text").set_text(text=FILE_NAME)
    if out:
        print("Success: input file name")
    wait()

    out = d(className="android.widget.FrameLayout",resourceId="com.google.android.inputmethod.latin:id/key_pos_ime_action").click()
    if not out:
        print("Success: click search button")
    wait()

    out = d(className="android.widget.FrameLayout",resourceId="com.google.android.inputmethod.latin:id/key_pos_ime_action").click()
    if not out:
        print("Success: click search button")
    wait()

    out = d(className="android.widget.TextView",resourceId="com.amaze.filemanager:id/firstline").click()
    if not out:
        print("Success: click file")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/md_title", text="Other").click()
    if not out:
        print("Success: click other")
    wait()

    out = d(className="android.widget.Button",resourceId="android:id/button_once").click()
    if not out:
        print("Sucess: click just once button")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)