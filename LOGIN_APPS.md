This file describes how to test the apps that required login by using the snapshot feature of Android emulator.
Please create a fresh emulator with 'Nexus 7' for each crash bug before do the following instructions.

```
$ cd scripts/
$ emulator -avd Android7.1 -no-window &
$ adb devices

List of devices attached
emulator-5554	device
```

```
$ bash -x copy_dummy_documents.sh emulator-5554

+ '[' 1 -eq 0 ']'
+ AVD_SERIAL=emulator-5554
+ adb -s emulator-5554 push ../dummy_documents/Android_logo.jpg /sdcard/Pictures/
../dummy_documents/Android_logo.jpg: 1 file pushed, 0 skipped. 265.3 MB/s (64185 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/Android_robot.png /sdcard/Pictures/
../dummy_documents/Android_robot.png: 1 file pushed, 0 skipped. 156.0 MB/s (13418 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/droidbot_utg.png /sdcard/Pictures/
../dummy_documents/droidbot_utg.png: 1 file pushed, 0 skipped. 1578.5 MB/s (269533 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/Heartbeat.mp3 /sdcard/Music/
../dummy_documents/Heartbeat.mp3: 1 file pushed, 0 skipped. 3237.9 MB/s (1739320 bytes in 0.001s)
+ adb -s emulator-5554 push ../dummy_documents/intermission.mp3 /sdcard/Music/
../dummy_documents/intermission.mp3: 1 file pushed, 0 skipped. 2437.7 MB/s (995735 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/sample_iPod.m4v /sdcard/Movies/
../dummy_documents/sample_iPod.m4v: 1 file pushed, 0 skipped. 3265.6 MB/s (2236480 bytes in 0.001s)
+ adb -s emulator-5554 push ../dummy_documents/sample_mpeg4.mp4 /sdcard/Movies/
../dummy_documents/sample_mpeg4.mp4: 1 file pushed, 0 skipped. 1598.5 MB/s (245779 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/sample_sorenson.mov /sdcard/Movies/
../dummy_documents/sample_sorenson.mov: 1 file pushed, 0 skipped. 995.8 MB/s (82395 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/sample.3gp /sdcard/Movies/
../dummy_documents/sample.3gp: 1 file pushed, 0 skipped. 235.0 MB/s (28561 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/DroidBot_documentation.docx /sdcard/Download/
../dummy_documents/DroidBot_documentation.docx: 1 file pushed, 0 skipped. 1160.3 MB/s (107623 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/DroidBot_documentation.pdf /sdcard/Download/
../dummy_documents/DroidBot_documentation.pdf: 1 file pushed, 0 skipped. 712.1 MB/s (69660 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/password.txt /sdcard/Download/
../dummy_documents/password.txt: 1 file pushed, 0 skipped. 1.6 MB/s (52 bytes in 0.000s)
+ adb -s emulator-5554 push ../dummy_documents/sample_3GPP.3gp.zip /sdcard/Download/
../dummy_documents/sample_3GPP.3gp.zip: 1 file pushed, 0 skipped. 249.9 MB/s (26491 bytes in 0.000s)
```

```
$ adb -s emulator-5554 install -g ../WordPress/WordPress-vanilla-debug--#8659.apk

$ python3 ../WordPress/login-#8659.py emulator-5554


wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
{'package': 'org.wordpress.android', 'activity': 'org.wordpress.android.ui.accounts.LoginActivity'}
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
[D 210827 22:22:49 __init__:600] kill process(ps): uiautomator
[D 210827 22:22:50 __init__:618] uiautomator-v2 is starting ... left: 40.0s
[D 210827 22:22:51 __init__:618] uiautomator-v2 is starting ... left: 39.0s
[D 210827 22:22:52 __init__:618] uiautomator-v2 is starting ... left: 38.0s
[D 210827 22:22:53 __init__:618] uiautomator-v2 is starting ... left: 37.0s
[D 210827 22:22:54 __init__:618] uiautomator-v2 is starting ... left: 36.0s
[D 210827 22:22:55 __init__:618] uiautomator-v2 is starting ... left: 35.0s
[D 210827 22:22:56 __init__:618] uiautomator-v2 is starting ... left: 34.0s
[I 210827 22:22:56 __init__:583] uiautomator back to normal
SUCCESS: press login button
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
SUCCESS: press login in via site address
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
SUCCESS: input site address
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
SUCCESS: press next
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
SUCCESS: input user name
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
SUCCESS: input password
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
SUCCESS: press next
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
wait 1 second ..
org.wordpress.android
org.wordpress.android.ui.accounts.LoginEpilogueActivity
****Login SUCCESS*****
../WordPress/login-#8659.py:76: DeprecationWarning: Call to deprecated method service. (You should use d.uiautomator.start() instead) -- Deprecated since version 3.0.0.
  d.service("uiautomator").stop()
../WordPress/login-#8659.py:78: DeprecationWarning: Call to deprecated method service. (You should use d.uiautomator.start() instead) -- Deprecated since version 3.0.0.
  out = d.service("uiautomator").running()
DISCONNECT UIAUTOMATOR2 SUCCESS
```

- Stop the machine (i.e., snapshot the machine state)

```
$ adb -s emulator-5554 emu kill
```

- Run a tool on this bug

```
python3 themis.py --no-headless --avd Android7.1 --apk ../nextcloud/nextcloud-#5173.apk --time 10m -o ../monkey-results/ --login ../nextcloud/login-#5173.py --monkey --snapshot
```

```
We've tested the login process in different network connection situations.
Due to the account issue, Frost cannot be tested in all threee industrial tools.

1. connection with google access

 commons/commons-2.11.0-#3244.apk                         success
 commons/commons-2.9.0-#2123.apk                          success
 commons/commons-2.6.7-#1391.apk     	                    success
 commons/commons-2.6.7-#1385.apk                          success   
 commons/commons-2.7.1-#1581.apk                          success
 Frost/Frost-debug-2.2.1-#1323.apk                        fail(account issue)
 MaterialFBook/MaterialFBook4.0.2-debug-#224.apk          no need for login
 nextcloud/nextcloud-#5173.apk         		                success                 
 nextcloud/nextcloud-#4026.apk          		              success
 nextcloud/nextcloud-#4792.apk         		                success
 nextcloud/nextcloud-#1918.apk                            success
 WordPress/WordPress-vanilla-debug--#8659.apk             success
 WordPress/WordPress-vanilla-debug--#7182.apk             success
 WordPress/WordPress-vanilla-debug--#6530.apk             success
 WordPress/WordPress-vanilla-debug--#11992.apk            success
 WordPress/WordPress-vanilla-debug--#11135.apk            success
 WordPress/WordPress-vanilla-debug--#10876.apk            success
 WordPress/WordPress-vanilla-debug--#10547.apk            success
 WordPress/WordPress-vanilla-debug--#10363.apk            success  
 WordPress/WordPress-vanilla-debug--#10302.apk            no need for login
 
 
 
2. connection without google access

 commons/commons-2.11.0-#3244.apk                         fail
 commons/commons-2.9.0-#2123.apk                          fail
 commons/commons-2.6.7-#1391.apk     	                    fail
 commons/commons-2.6.7-#1385.apk                          fail   
 commons/commons-2.7.1-#1581.apk                          fail
 Frost/Frost-debug-2.2.1-#1323.apk                        fail(account issue)
 MaterialFBook/MaterialFBook4.0.2-debug-#224.apk          no need for login
 nextcloud/nextcloud-#5173.apk         		                success                 
 nextcloud/nextcloud-#4026.apk          		              success
 nextcloud/nextcloud-#4792.apk         		                success
 nextcloud/nextcloud-#1918.apk                            success
 WordPress/WordPress-vanilla-debug--#8659.apk             success
 WordPress/WordPress-vanilla-debug--#7182.apk             success
 WordPress/WordPress-vanilla-debug--#6530.apk             success
 WordPress/WordPress-vanilla-debug--#11992.apk            success
 WordPress/WordPress-vanilla-debug--#11135.apk            success
 WordPress/WordPress-vanilla-debug--#10876.apk            success
 WordPress/WordPress-vanilla-debug--#10547.apk            success
 WordPress/WordPress-vanilla-debug--#10363.apk            success  
 WordPress/WordPress-vanilla-debug--#10302.apk            no need for login
