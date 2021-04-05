
For #1391: the issue was described in [#1329](https://github.com/commons-app/apps-android-commons/issues/1329)

    ```6. Bug: if you click one of nearby markers and make information bottom sheet visible, then go to settings and change theme, app will crash when you re-start nearby activity. Log is at below comment PR #1391```

For #1385: the issue was also described in [#1329](https://github.com/commons-app/apps-android-commons/issues/1329)

    ```5. Crash on orientation change crashes when list view is open and orinetation changed. PR: #1385```

For #1385: according to the bug report, it is necessary to open the options of the nearby list, but we find sometimes it may not be necessary. 


For #1581: do not grant permission when installation (it will be more easier to trigger the bug if do not grant runtime permission when installation, but it is 
not necessary)

Better to add some pics under /sdcard/DCIM/Camera/ (but not necessary, because the app could also take pics by itself)

===== Account Info =======

Test Account 1: DroidFuzzing1 / droid.fuzzing1
Test Account 2: DroidFuzzing2 / droid.fuzzing2
Test Account 2: DroidFuzzing3 / droid.fuzzing3
Test Account 2: DroidFuzzing4 / droid.fuzzing4
Test Account 2: DroidFuzzing5 / droid.fuzzing5

===== GUI Info =======

2.11.0

fr.free.nrw.commons:id/finishTutorialButton / YES!

fr.free.nrw.commons:id/login_username / Username
fr.free.nrw.commons:id/login_password / Password

fr.free.nrw.commons:id/login_button / LOG IN


2.9.0

fr.free.nrw.commons:id/welcomeYesButton / YES!

fr.free.nrw.commons:id/loginUsername
fr.free.nrw.commons:id/loginPassword


fr.free.nrw.commons:id/loginButton / LOG IN


2.7.1

fr.free.nrw.commons.debug:id/welcomeYesButton / YES!

fr.free.nrw.commons:id/loginUsername
fr.free.nrw.commons:id/loginPassword


fr.free.nrw.commons:id/loginButton / LOG IN


2.6.7

fr.free.nrw.commons.debug:id/welcomeYesButton / YES!

fr.free.nrw.commons:id/loginUsername
fr.free.nrw.commons:id/loginPassword


fr.free.nrw.commons:id/loginButton / LOG IN
