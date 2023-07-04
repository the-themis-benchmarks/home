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

    out = d(resourceId="com.amaze.filemanager:id/firstline", text="Download").click()
    if out:
        print("Success: click Download Folder")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/properties").click()
    if not out:
        print("Success: click properties of the .tar.gz file")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[9]').click()
    if not out:
        print("Success: click extract")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
