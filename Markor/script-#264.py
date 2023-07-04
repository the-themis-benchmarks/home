# bug reproduction script for bug #4451of ankidroid
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


    d.app_start("net.gsantner.markor")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "net.gsantner.markor":
            break
        time.sleep(2)
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: click More options")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: click Create Folder")
    wait()

    out = d(resourceId="net.gsantner.markor:id/create_folder_dialog__folder_name").set_text("test")
    if not out:
        print("Success: enter folder name")
    wait()

    out = d(resourceId="android:id/button1").click()
    if not out:
        print("Success: click Ok")
    wait()

    out = d(text="test").long_click()
    if not out:
        print("Success: long click a folder")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: click More options")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[2]').click()
    if not out:
        print("Success: click info")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
