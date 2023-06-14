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

    out = d(resourceId="org.totschnig.myexpenses.debug:id/MANAGE_TEMPLATES_COMMAND").click()
    if not out:
        print("Success: open templates")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND").click()
    if not out:
        print("Success: create a template")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/Title").set_text("test")
    if not out:
        print("Success: enter template title")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/AmountEditText").set_text("555")
    if not out:
        print("Success: enter payee")
    wait()

    out = d.xpath('//*[@resource-id="org.totschnig.myexpenses.debug:id/PlanRow"]/android.view.ViewGroup[1]').click()
    if not out:
        print("Success: choose plan")
    wait()

    out = d(resourceId="android:id/text1", text="Daily").click()
    if not out:
        print("Success: choose Daily")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/CREATE_COMMAND").click()
    if not out:
        print("Success: click create")
    wait()

    out = d(resourceId="org.totschnig.myexpenses.debug:id/PLANNER_COMMAND").click()
    if not out:
        print("Success: click Planner")
    wait()

    out = d.xpath('//*[@resource-id="org.totschnig.myexpenses.debug:id/recycler_view"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]').long_click()
    if not out:
        print("Success: long click a plan")
    wait()

    out = d.press("recent")
    if not out:
        print("Success: minimize the app")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
