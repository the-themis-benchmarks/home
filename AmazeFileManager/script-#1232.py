# bug reproduction script for bug #1232 of AFM
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

    out = d(className="android.widget.TextView", text="Alarms").long_click()
    if out:
        print("Success: long click Alarms")
    wait()

    out = d(className="android.widget.TextView", resourceId="com.amaze.filemanager:id/cpy").click()
    if not out:
        print("Success: press copy")
    wait()

    out = d(className="android.widget.ImageButton", description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(className="android.widget.ListView", resourceId="com.amaze.filemanager:id/menu_drawer")\
        .child(index="2").click()
    if not out:
        print("Success: press sdcard")
    wait()

    out = d(className="android.widget.TextView", resourceId="com.amaze.filemanager:id/paste").click()
    if not out:
        print("Success: press paste")
    wait()

    out = d(className="android.widget.TextView", text="OPEN").click()
    if not out:
        print("Success: press paste")
    wait(5)

    out = d(className="android.widget.TextView", text="SDCARD").click()
    if not out:
        print("Success: press sdcard")
    wait()

    out = d(className="android.widget.Button", text="SELECT").click()
    if not out:
        print("Success: press SELECT")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
