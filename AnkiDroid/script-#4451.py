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

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(text="Settings").click()
    if not out:
        print("Success: press settings")
    wait()

    out = d(text="Gestures").click()
    if not out:
        print("Success: press gentures")
    wait()

    out = d(resourceId="android:id/checkbox").click()
    if not out:
        print("Success: check enable gestures")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(text="Reviewing").click()
    if not out:
        print("Success: press reviewing")
    wait()

    out = d(className="android.widget.ListView").swipe("up", steps=10)
    if not out:
        print("Success: scroll down")
    wait(1)

    out = d(text="Fullscreen mode").click()
    if not out:
        print("Success: press full screen mode")
    wait()

    out = d(text="Hide the system bars and answer buttons").click()
    if not out:
        print("Success: press Hide the system bars and answer buttons")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press navigation")
    wait()

    out = d(resourceId="com.ichi2.anki:id/fab_expand_menu_button").click()
    if not out:
        print("Success: press fab button")
    wait()

    out = d(resourceId="com.ichi2.anki:id/add_note_action").click()
    if not out:
        print("Success: press add")
    wait()

    out = d(className="android.widget.LinearLayout",
            resourceId="com.ichi2.anki:id/CardEditorEditFieldsLayout") \
        .child(className="android.widget.RelativeLayout", index="1") \
        .child(resourceId="com.ichi2.anki:id/id_note_editText").set_text("test")
    if out:
        print("Success: set front text")
    wait()

    out = d(className="android.widget.LinearLayout",
            resourceId="com.ichi2.anki:id/CardEditorEditFieldsLayout") \
        .child(className="android.widget.RelativeLayout", index="3") \
        .child(resourceId="com.ichi2.anki:id/id_note_editText").set_text("you")
    if out:
        print("Success: set back text")
    wait()

    out = d(resourceId="com.ichi2.anki:id/action_save").click()
    if not out:
        print("Success: press save")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press back")
    wait()

    out = d(text="Default").click()
    if not out:
        print("Success: press default")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
