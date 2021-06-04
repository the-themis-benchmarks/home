# bug reproduction script for bug #114 of Scarlet-Notes
import os
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

    d.app_start("com.bijoysingh.quicknote")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.bijoysingh.quicknote":
            break
        #d.app_start("org.odk.collect.android")
        time.sleep(2)
    wait()

    out = d(resourceId="com.bijoysingh.quicknote:id/lithoBottomToolbar").child(index="0").child(index="1").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Add Notebook").set_text("myBook")
    if out:
        print("SUCCESS")
    wait()

    d.press("enter")
    print("SUCCESS")
    wait()

    out = d(text="myBook").click()
    if out:
        print("SUCCESS")
    wait()


    out = d(resourceId="com.bijoysingh.quicknote:id/lithoBottomToolbar", index="2").child(index="0").child(index="3").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Add Heading…").set_text("Note1")
    if out:
        print("SUCCESS")
    wait()

    d.press("back")
    print("SUCCESS")
    wait()

    d.press("back")
    print("SUCCESS")
    wait()

    out = d(resourceId="com.bijoysingh.quicknote:id/lithoBottomToolbar", index="2").child(index="0").child(index="3").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Add Heading…").set_text("Note2")
    if out:
        print("SUCCESS")
    wait()

    d.press("back")
    print("SUCCESS")
    wait()

    d.press("back")
    print("SUCCESS")
    wait()

    out = d(text="Note1").long_click()
    if out:
        print("SUCCESS")
    wait()

    d.press("back")
    wait()

    out = d(text="Lock Note").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="com.bijoysingh.quicknote:id/lithoBottomToolbar", index="2").child(index="0").child(index="0").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(text="Locked").click()
    if not out:
        print("SUCCESS")
    wait()

    out = d(resourceId="com.bijoysingh.quicknote:id/lithoPreBottomToolbar", index="1").click(offset=(0.05, 0.5))
    if not out:
        print("SUCCESS")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
