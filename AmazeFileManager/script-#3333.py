# bug reproduction script for bug #1232 of AFM
import sys
import time

import uiautomator2 as u2

# For this bug, need to put more than two .zip/.rar/.gz/.apk(>500MB)... files in Download folder
# Replace these two ↓ with your own file names

FIRST_FILE_NAME = "android-studio-2020.3.1.22-windows.zip"
SECOND_FILE_NAME = "gz.tar.gz"

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

    out = d(description="Navigate up").click()
    if out:
        print("Success: click Navigation")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/design_menu_item_text", text="Download").click()
    if not out:
        print("Success: click Download")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/firstline", text=FIRST_FILE_NAME).long_click()
    if not out:
        print("Success: longclick first file")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/firstline", text=SECOND_FILE_NAME).click()
    if not out:
        print("Success: click second file")
    wait()

    out = d.xpath('//*[@resource-id="com.amaze.filemanager:id/listView"]/android.widget.RelativeLayout[4]/android.widget.ImageButton[1]').click()
    if not out:
        print("Success: click more options")
    wait()

    out = d(scrollable=True).scroll.toEnd()
    if not out:
        print("Success: scroll to click extract")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[8]').click()
    if not out:
        print("Success: click extract")
    wait()

    out = d.drag(0.2,0,0.2,0.872)
    if not out:
        print("Success: open notifications")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/notification_service_progressBar_small").click()
    if not out:
        print("Success: click Amaze extract progress")
    wait()

    out = d(resourceId="com.amaze.filemanager:id/delete_button").click()
    if not out:
        print("Success: [Optional] cancel the progress")
    wait()



    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
