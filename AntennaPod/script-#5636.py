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


    d.app_start("de.danoeh.antennapod.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "de.danoeh.antennapod.debug":
            break
        time.sleep(2)
    wait()

    out = d(description="Open menu").click()
    if not out:
        print("Success: open navigation")
    wait()

    out = d(resourceId="de.danoeh.antennapod.debug:id/txtvTitle", text="Subscriptions").click()
    if not out:
        print("Success: click Subscriptions")
    wait()

    out = d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/subscriptions_grid"]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: click a podcast in Subcriptions")
    wait()

    out = d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/recyclerView"]/android.widget.FrameLayout[1]').click()
    if not out:
        print("Success: click an episode")
    wait()

    out = d(resourceId="de.danoeh.antennapod.debug:id/butAction1Text").click()
    if not out:
        print("Success: stream")
    wait()

    out = d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/audioplayerFragment"]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]').click()
    if not out:
        print("Success: enter the playback interface")
    wait()

    out = d.xpath('//*[@resource-id="de.danoeh.antennapod.debug:id/audioplayerFragment"]/android.widget.RelativeLayout[1]/android.view.ViewGroup[1]/androidx.appcompat.widget.LinearLayoutCompat[1]/android.widget.ImageView[1]').click()
    if not out:
        print("Success: click more")
    wait()

    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: click Share")
    wait()

    out = d.press("recent")
    if not out:
        print("Success: minimize the app")
    wait()

    # out = d.app_start("de.danoeh.antennapod.debug")
    # if not out:
    #     print("Success: click OK")
    # wait()



    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
