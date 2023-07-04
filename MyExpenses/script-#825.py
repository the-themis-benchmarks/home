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


    d.app_start("org.totschnig.myexpenses.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "org.totschnig.myexpenses.debug":
            break
        time.sleep(2)
    wait()

    out = d(description="More options").click()
    if not out:
        print("Success: click More options")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[10]').click()
    if not out:
        print("Success: open Settings")
    wait()

    out = d(resourceId="android:id/title", text="Categories").click()
    if not out:
        print("Success: open Categories")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/SETUP_CATEGORIES_DEFAULT_COMMAND").click()
    if not out:
        print("Success: set up default categories")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/SEARCH_COMMAND").click()
    if not out:
        print("Success: click search")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/search_src_text").set_text("car")
    if not out:
        print("Success: search for car")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/label", text="Car").long_click()
    if not out:
        print("Success: long click the car category")
    wait()

    out = d.xpath('//*[@resource-id="org.totschnig.myexpenses.debug:id/toolbar"]/androidx.appcompat.widget.LinearLayoutCompat[2]/android.widget.ImageView[1]').click()
    if not out:
        print("Success: click More options")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[3]').click()
    if not out:
        print("Success: click move")
    wait()

    out = d(resourceId="android:id/text1", text="Care").click()
    if not out:
        print("Success: move to Care")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
