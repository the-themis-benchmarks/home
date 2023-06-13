# bug reproduction script for bug #4451of ankidroid
import sys
import time

import uiautomator2 as u2

# This bug needs data(enough cards to support swiping pages), set DATA_FLAG = 1 to run the script with data generation
# Please set LAST_CARD_TEXT with the "Question" text of your last card, the default value is "end"
DATA_FLAG = 1
LAST_CARD_TEXT = "end"

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

    if DATA_FLAG == 1:
        out = d(description="Navigate up").click()
        if not out:
            print("Success: click Navigation")
        wait()

        out = d(resourceId="com.ichi2.anki:id/design_menu_item_text", text="Card browser").click()
        if not out:
            print("Success: enter Card browser")
        wait()

        out = d(resourceId="com.ichi2.anki:id/action_add_note_from_card_browser").click()
        if not out:
            print("Success: add notes")
        wait()

        out = d(resourceId="com.ichi2.anki:id/id_note_editText", description="Front").set_text("super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph")
        if not out:
            print("Success: add a note")
        wait()

        out = d(resourceId="com.ichi2.anki:id/action_save").click()
        if not out:
            print("Success: click save")
        wait()

        out = d(resourceId="com.ichi2.anki:id/id_note_editText", description="Front").set_text("super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph")
        if not out:
            print("Success: add a note")
        wait()

        out = d(resourceId="com.ichi2.anki:id/action_save").click()
        if not out:
            print("Success: click save")
        wait()

        out = d(resourceId="com.ichi2.anki:id/id_note_editText", description="Front").set_text("end")
        if not out:
            print("Success: add a note")
        wait()

        out = d(resourceId="com.ichi2.anki:id/action_save").click()
        if not out:
            print("Success: click save")
        wait()

        # out = d(resourceId="com.ichi2.anki:id/id_note_editText", description="Front").set_text("super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph super long paragraph")
        # if not out:
        #     print("Success: add a note")
        # wait()

        # out = d(resourceId="com.ichi2.anki:id/action_save").click()
        # if not out:
        #     print("Success: click save")
        # wait()

        out = d(description="Navigate up").click()
        if not out:
            print("Success: click back")
        wait()

        out = d(description="More options").click()
        if not out:
            print("Success: click More options")
        wait()

        out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[1]').click()
        if not out:
            print("Success: click Change display order")
        wait()

        out = d(resourceId="com.ichi2.anki:id/md_title", text="No sorting (faster)").click()
        if not out:
            print("Success: display by created time")
        wait()

        out = d(description="Navigate up").click()
        if not out:
            print("Success: click Navigation")
        wait()

        out = d(resourceId="com.ichi2.anki:id/design_menu_item_text", text="Decks").click()
        if not out:
            print("Success: return to Decks")
        wait()

    out = d(description="Navigate up").click()
    if not out:
        print("Success: click Navigation")
    wait()

    out = d(resourceId="com.ichi2.anki:id/design_menu_item_text", text="Card browser").click()
    if not out:
        print("Success: enter Card browser")
    wait()

    out = d(resourceId="com.ichi2.anki:id/card_sfld").long_click()
    if not out:
        print("Success: long click the first card")
    wait()

    out = d.swipe_ext("up", 1)
    if not out:
        print("Success: swipe to the last card")
    wait()

    out = d.swipe_ext("up", 1)
    if not out:
        print("Success: swipe to the last card")
    wait()

    out = d.swipe_ext("up", 1)
    if not out:
        print("Success: swipe to the last card")
    wait()

    d(resourceId="com.ichi2.anki:id/card_sfld", text=LAST_CARD_TEXT).long_click()
    if not out:
        print("Success: long click the last card")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
