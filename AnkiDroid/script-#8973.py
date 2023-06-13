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


    d.app_start("com.ichi2.anki")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.ichi2.anki":
            break
        time.sleep(2)
    wait()

    out = d(resourceId="com.ichi2.anki:id/fab_main").click()
    if not out:
        print("Success: click add")
    wait()

    out = d(resourceId="com.ichi2.anki:id/add_note_action").click()
    if not out:
        print("Success: click add note")
    wait()

    out = d.xpath('//*[@resource-id="com.android.systemui:id/ends_group"]/android.widget.RelativeLayout[2]').click()
    if not out:
        print("Success: dismiss the keyboard?")
    wait()

    out = d(resourceId="com.ichi2.anki:id/CardEditorTagText").click()
    if not out:
        print("Success: click Tags")
    wait()

    out = d(resourceId="com.ichi2.anki:id/tags_dialog_action_add").click()
    if not out:
        print("Success: add a tag")
    wait()

    out = d(resourceId="android:id/input").set_text("test")
    if not out:
        print("Success: enter new tag name")
    wait()

    out = d.press("home")
    if not out:
        print("Success: return home")
    wait()

    out = d.app_start("com.ichi2.anki")
    if not out:
        print("Success: open app again")
    wait()

    out = d(resourceId="com.ichi2.anki:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: click OK")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
