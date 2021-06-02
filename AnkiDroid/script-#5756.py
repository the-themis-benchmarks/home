# bug reproduction script for bug #5756 of ankidroid
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
        .child(resourceId="com.ichi2.anki:id/id_note_editText").set_text("aaa")
    if not out:
        print("Success: set front text")
    wait()

    out = d(resourceId="com.ichi2.anki:id/action_save").click()
    if not out:
        print("Success: press save")
    wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: press back")
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: press more options")
    wait()

    out = d(text="Create filtered deck").click()
    if not out:
        print("Success: press Create filtered deck")
    wait()

    out = d(text="CREATE").click()
    if not out:
        print("Success: press CREATE")
    wait()

    out = d(text="cards selected by").click()
    if not out:
        print("Success: press cards selected by")
    wait()

    out = d(text="Random").click()
    if not out:
        print("Success: Random")
    wait()

    out = d(text="cards selected by").click()
    if not out:
        print("Success: press cards selected by")
    wait()

    out = d(text="Oldest seen first").click()
    if not out:
        print("Success: Oldest seen first")
    wait()

    x, y = d(description="Navigate up").center()
    d.double_click(x, y, duration=0.5)
    if not out:
        print("Success: press back")
    wait()

    out = d(description="", resourceId="", className="android.widget.ImageButton").click()
    if not out:
        print("Success: press back")
    wait()

    out = d(text="Filtered Deck 1").click()
    if not out:
        print("Success: Filtered Deck 1")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
