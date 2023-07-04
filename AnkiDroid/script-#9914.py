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
        print("Success: click navigation")
    wait()

    out = d(resourceId="com.ichi2.anki:id/design_menu_item_text", text="Statistics").click()
    if not out:
        print("Success: click Statistics")
    wait()

    out = d(resourceId="com.ichi2.anki:id/dropdown_deck_name").click()
    if not out:
        print("Success: choose a deck")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
