# The Themis Benchmark

Themis is a collection of real-world, reproducible crash bugs (collected from 
open-source Android apps) and a unified, extensible infrastructure 
for benchmarking automated GUI testing for Android and beyond. 

# Contents of Themis

## Themis's bug dataset

Themis now contains *52* reproducible crash bugs. All these bugs are labeled by
the app developers as "critical bugs" (i.e., important bugs), which affected the 
major app functionalities and the larger percentage of app users.

For each bug, we provide:

- An executable APK (Jacoco-instrumented for coverage collection),
 
- A bug-reproducing script (python-based script for bug inspection) and a video 

- The stack trace of the bug 

- Metadata for supporting evaluation (e.g., bug explanation, login script, configuration files used by the Themis's infrastructure)

- the app source code w.r.t each bug 


### List of crash bugs
Issue Id | App | Bug report, data | Version | Category | GitHub Stars | Reproducible? | Network? | Login? | Setting? 
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
1 | *[AmazeFileManager](https://github.com/TeamAmaze/AmazeFileManager)* | [#1837](https://github.com/TeamAmaze/AmazeFileManager/issues/1837), [data](https://github.com/the-themis-benchmarks/home/tree/master/AmazeFileManager) | 3.4.2 | File Manager | 3.0K | 6.0/7.1 | no | no| no 
2 | *[AmazeFileManager](https://github.com/TeamAmaze/AmazeFileManager)* | [#1796](https://github.com/TeamAmaze/AmazeFileManager/issues/1796), [data](https://github.com/the-themis-benchmarks/home/tree/master/AmazeFileManager) | 3.3.2  | File Manager | 3.0K | 4.4/6.0/7.1 | no | no  | no 
3 | *[AmazeFileManager](https://github.com/TeamAmaze/AmazeFileManager)* | [#1558](https://github.com/TeamAmaze/AmazeFileManager/issues/1558), [data](https://github.com/the-themis-benchmarks/home/tree/master/AmazeFileManager) | 3.3.2  | File Manager | 3.0K | 6.0/7.1 | no | no | no 
4 | *[AmazeFileManager](https://github.com/TeamAmaze/AmazeFileManager)* | [#1232](https://github.com/TeamAmaze/AmazeFileManager/issues/1232), [data](https://github.com/the-themis-benchmarks/home/tree/master/AmazeFileManager) | 3.2.1  | File Manager | 3.0K | 6.0/7.1 | no | no | no  
5 | *[ActivityDiary](https://github.com/ramack/ActivityDiary)* | [#285](https://github.com/ramack/ActivityDiary/issues/285), [data](https://github.com/the-themis-benchmarks/home/tree/master/ActivityDiary) | 1.4.0  | Personal Diary | 55 | 6.0/7.1 | no | no | no
6 | *[ActivityDiary](https://github.com/ramack/ActivityDiary)* | [#118](https://github.com/ramack/ActivityDiary/issues/118), [data](https://github.com/the-themis-benchmarks/home/tree/master/ActivityDiary) | 1.1.8  | Personal Diary | 55 | 6.0/7.1 | no | no | no
7 | *[and-bible](https://github.com/AndBible/and-bible)* | [#375](https://github.com/AndBible/and-bible/issues/375), [data](https://github.com/the-themis-benchmarks/home/tree/master/and-bible) | 3.1.309  | Bible Reader | 231 | 4.4/6.0/7.1 | yes | no | no 
8 | *[and-bible](https://github.com/AndBible/and-bible)* | [#697](https://github.com/AndBible/and-bible/issues/697), [data](https://github.com/the-themis-benchmarks/home/tree/master/and-bible) | 3.2.369 | Bible Reader | 231 | 6.0/7.1 | yes | no | no 
9 | *[and-bible](https://github.com/AndBible/and-bible)* | [#261](https://github.com/AndBible/and-bible/issues/261), [data](https://github.com/the-themis-benchmarks/home/tree/master/and-bible) | 3.0.286  | Bible Reader | 231 | 6.0/7.1 | yes | no | no 
10 | *[and-bible](https://github.com/AndBible/and-bible)* | [#703](https://github.com/AndBible/and-bible/issues/703), [data](https://github.com/the-themis-benchmarks/home/tree/master/and-bible) | 3.3.377  | Bible Reader | 231 | 6.0/7.1 | yes | no | no 
11 | *[and-bible](https://github.com/AndBible/and-bible)* |  [#480](https://github.com/AndBible/and-bible/issues/480), [data](https://github.com/the-themis-benchmarks/home/tree/master/and-bible) | 3.2.327  | Bible Reader | 231 | 4.4/6.0/7.1 | yes | no | no 
12 | *[Anki-Android](https://github.com/ankidroid/Anki-Android)* | [#4707](https://github.com/ankidroid/Anki-Android/issues/4707), [data](https://github.com/the-themis-benchmarks/home/tree/master/AnkiDroid) | 2.9alpha4 | Card Learning | 2.8K | 7.1 | no | no | no
13 | *[Anki-Android](https://github.com/ankidroid/Anki-Android)* | [#5638](https://github.com/ankidroid/Anki-Android/issues/5638), [data](https://github.com/the-themis-benchmarks/home/tree/master/AnkiDroid) | 2.9.1 | Card Learning | 2.8K | 6.0/7.1 | no | no | no 
14 | *[Anki-Android](https://github.com/ankidroid/Anki-Android)* | [#4200](https://github.com/ankidroid/Anki-Android/issues/4200), [data](https://github.com/the-themis-benchmarks/home/tree/master/AnkiDroid) | 2.6  | Card Learning | 2.8K | 4.4/6.0/7.1 | no | no | no 
15 | *[Anki-Android](https://github.com/ankidroid/Anki-Android)* | [#4451](https://github.com/ankidroid/Anki-Android/issues/4451), [data](https://github.com/the-themis-benchmarks/home/tree/master/AnkiDroid) | 2.7 | Card Learning | 2.8K | 4.4/6.0/7.1 | no | no | no 
16 | *[Anki-Android](https://github.com/ankidroid/Anki-Android)* | [#6145](https://github.com/ankidroid/Anki-Android/issues/6145), [data](https://github.com/the-themis-benchmarks/home/tree/master/AnkiDroid) | 2.10  | Card Learning | 2.8K | 4.4/6.0/7.1 | no | no | yes 
17 | *[Anki-Android](https://github.com/ankidroid/Anki-Android)* | [#5756](https://github.com/ankidroid/Anki-Android/issues/5756), [data](https://github.com/the-themis-benchmarks/home/tree/master/AnkiDroid) | 2.9.4  | Card Learning | 2.8K | 4.4/6.0/7.1 | no | no | no 
18 | *[Anki-Android](https://github.com/ankidroid/Anki-Android)* | [#4977](https://github.com/ankidroid/Anki-Android/issues/4977), [data](https://github.com/the-themis-benchmarks/home/tree/master/AnkiDroid) | 2.9  | Card Learning | 2.8K | 4.4/6.0/7.1 | no | no | no 
19 | *[APhotoManager](https://github.com/k3b/APhotoManager)* | [#116](https://github.com/k3b/APhotoManager/issues/116), [data](https://github.com/the-themis-benchmarks/home/tree/master/APhotoManager)| 0.6.4  | Photo Manager | 148 | 4.4/6.0/7.1 | no | no | no
20 | *[collect](https://github.com/getodk/collect)* | [#3222](https://github.com/getodk/collect/issues/3222), [data](https://github.com/the-themis-benchmarks/home/tree/master/collect) | 1.23.0  | Form Data Collector | 528 | 4.4/6.0/7.1 | yes | no | no
21 | *[commons](https://github.com/commons-app/apps-android-commons)* | [#3244](https://github.com/commons-app/apps-android-commons/issues/3244), [data](https://github.com/the-themis-benchmarks/home/tree/master/commons) | 2.11.0  | Wikimedia | 601 | 6.0/7.1 | yes | yes | no 
22 | *[commons](https://github.com/commons-app/apps-android-commons)* | [#2123](https://github.com/commons-app/apps-android-commons/issues/2123), [data](https://github.com/the-themis-benchmarks/home/tree/master/commons)| 2.9.0  | Wikimedia | 601 | 6.0/7.1 | yes | yes | no 
23 | *[commons](https://github.com/commons-app/apps-android-commons)* | [#1391](https://github.com/commons-app/apps-android-commons/pull/1391)(Ref:[#1329](https://github.com/commons-app/apps-android-commons/issues/1329)), [data](https://github.com/the-themis-benchmarks/home/tree/master/commons) | 2.6.7  | Wikimedia | 601 | 6.0/7.1 | yes | yes | no 
24 | *[commons](https://github.com/commons-app/apps-android-commons)* | [#1385](https://github.com/commons-app/apps-android-commons/pull/1385)(Ref:[#1329](https://github.com/commons-app/apps-android-commons/issues/1329)), [data](https://github.com/the-themis-benchmarks/home/tree/master/commons) | 2.6.7  | Wikimedia | 601 | 6.0/7.1 | yes | yes | no 
25 | *[commons](https://github.com/commons-app/apps-android-commons)* | [#1581](https://github.com/commons-app/apps-android-commons/issues/1581), [data](https://github.com/the-themis-benchmarks/home/tree/master/commons) | 2.7.1  | Wikimedia | 601 | 6.0/7.1 | yes | yes | yes 
26 | *[FirefoxLite](https://github.com/mozilla-tw/FirefoxLite)* | [#4881](https://github.com/mozilla-tw/FirefoxLite/issues/4881), [data](https://github.com/the-themis-benchmarks/home/tree/master/FirefoxLite) | 2.1.12 | Browser | 231 | 6.0/7.1 | yes | no | no 
27 | *[FirefoxLite](https://github.com/mozilla-tw/FirefoxLite)* | [#5085](https://github.com/mozilla-tw/FirefoxLite/issues/5085), [data](https://github.com/the-themis-benchmarks/home/tree/master/FirefoxLite) | 2.1.20  | Browser | 231 | 6.0/7.1 | yes | no | no 
28 | *[FirefoxLite](https://github.com/mozilla-tw/FirefoxLite)* | [#4942](https://github.com/mozilla-tw/FirefoxLite/issues/4942), [data](https://github.com/the-themis-benchmarks/home/tree/master/FirefoxLite) | 2.1.16  | Browser | 231 | 6.0/7.1 | yes | no | no
29 | *[Frost-for-Facebook](https://github.com/AllanWang/Frost-for-Facebook)* | [#1323](https://github.com/AllanWang/Frost-for-Facebook/issues/1323), [data](https://github.com/the-themis-benchmarks/home/tree/master/Frost-for-Facebook) | 2.2.1 | Facebook Client | 377 | 6.0/7.1 | yes | yes | yes  
30 | *[geohashdroid](https://github.com/CaptainSpam/geohashdroid)* | [#73](https://github.com/CaptainSpam/geohashdroid/issues/73), [data](https://github.com/the-themis-benchmarks/home/tree/master/geohashdroid) | 0.9.4 | Geohash | 13 | 4.4/6.0/7.1 | no | no | no
31 | *[MaterialFBook](https://github.com/ZeeRooo/MaterialFBook)* | [#224](https://github.com/ZeeRooo/MaterialFBook/issues/224), [data](https://github.com/the-themis-benchmarks/home/tree/master/MaterialFBook) | 4.0.2  | Social | 122 | 6.0/7.1 | yes | yes | no
32 | *[nextcloud](https://github.com/nextcloud/android)* |  [#5173](https://github.com/nextcloud/android/issues/5173), [data](https://github.com/the-themis-benchmarks/home/tree/master/nextcloud) | 3.10.0  | Productivity | 1.9K | 6.0/7.1 | yes | yes | no 
33 | *[nextcloud](https://github.com/nextcloud/android)* | [#4026](https://github.com/nextcloud/android/issues/4026), [data](https://github.com/the-themis-benchmarks/home/tree/master/nextcloud) | 3.6.1  | Productivity | 1.9K | 6.0/7.1 | yes | yes | no
34 | *[nextcloud](https://github.com/nextcloud/android)* | [#4792](https://github.com/nextcloud/android/issues/4792), [data](https://github.com/the-themis-benchmarks/home/tree/master/nextcloud) | 3.9.2  | Productivity | 1.9K | 4.4/6.0/7.1 | yes | yes | no 
35 | *[nextcloud](https://github.com/nextcloud/android)* | [#1918](https://github.com/nextcloud/android/issues/1918), [data](https://github.com/the-themis-benchmarks/home/tree/master/nextcloud) | 2.0.0 | Productivity | 1.9K | 6.0/7.1 | yes | yes | no
36 | *[Omni-Notes](https://github.com/federicoiosue/Omni-Notes)* | [#745](https://github.com/federicoiosue/Omni-Notes/issues/745), [data](https://github.com/the-themis-benchmarks/home/tree/master/Omni-Notes) | 6.1.0  | Notebook | 2.1K | 4.4/6.0/7.1 | no | no | no    
37 | *[open-event-attendee](https://github.com/fossasia/open-event-attendee-android)* | [#2198](https://github.com/fossasia/open-event-attendee-android/issues/2198), [data](https://github.com/the-themis-benchmarks/home/tree/master/open-event-attendee-android) | 0.5 | Social Events | 1.5K | 6.0/7.1 | yes | no | no 
38 | *[openlauncher](https://github.com/OpenLauncherTeam/openlauncher)* | [#67](https://github.com/OpenLauncherTeam/openlauncher/issues/67)(Ref:[#250](https://github.com/jroal/a2dpvolume/issues/250)), [data](https://github.com/the-themis-benchmarks/home/tree/master/openlauncher) | 0.3.1  | App Launcher | 256 | 6.0/7.1 | no | no |  yes
39 | *[osmeditor4android](https://github.com/MarcusWolschon/osmeditor4android)* | [#729](https://github.com/MarcusWolschon/osmeditor4android/issues/729), [data](https://github.com/the-themis-benchmarks/home/tree/master/osmeditor4android) | 11.0.0  | Map | 171 | 4.4/6.0/7.1 | no | no | no 
40 | *[osmeditor4android](https://github.com/MarcusWolschon/osmeditor4android)* | [#637](https://github.com/MarcusWolschon/osmeditor4android/issues/637), [data](https://github.com/the-themis-benchmarks/home/tree/master/osmeditor4android) | 0.9.10  | Map | 171 | 6.0/7.1 | no | no | no
41 | *[Phonograph](https://github.com/kabouzeid/Phonograph)* | [#112](https://github.com/kabouzeid/Phonograph/issues/112), [data](https://github.com/the-themis-benchmarks/home/tree/master/Phonograph) | 0.15.0  | Music Player | 2.4K | 4.4/6.0/7.1 | no | no | no 
42 | *[Scarlet-Notes](https://github.com/BijoySingh/Scarlet-Notes)* | [#114](https://github.com/BijoySingh/Scarlet-Notes/issues/114), [data](https://github.com/the-themis-benchmarks/home/tree/master/Scarlet-Notes) | 6.9.5 | Notebook | 272 | 4.4/6.0/7.1 | no | no | no   
43 | *[sunflower](https://github.com/android/sunflower)* | [#239](https://github.com/android/sunflower/issues/239), [data](https://github.com/the-themis-benchmarks/home/tree/master/sunflower)  | 0.1.6  | Utility Tool | 12K | 4.4/6.0/7.1 | no | no | no 
44 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#8659](https://github.com/wordpress-mobile/WordPress-Android/issues/8659), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 11.3 | Social | 2.3K | 6.0/7.1 | yes | yes | no 
45 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#7182](https://github.com/wordpress-mobile/WordPress-Android/issues/7182), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 9.2  | Social | 2.3K  | 4.4/6.0/7.1 | yes | yes | no 
46 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#6530](https://github.com/wordpress-mobile/WordPress-Android/issues/6530), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 8.1  | Social | 2.3K | 4.4/6.0/7.1 | yes | yes | no 
47 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#11992](https://github.com/wordpress-mobile/WordPress-Android/issues/11992), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 14.9  | Social | 2.3K | 6.0/7.1 | yes | yes | no
48 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#11135](https://github.com/wordpress-mobile/WordPress-Android/issues/11135), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 13.6  | Social | 2.3K | 6.0/7.1 | yes | yes | no 
49 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#10876](https://github.com/wordpress-mobile/WordPress-Android/issues/10876), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 13.7  | Social | 2.3K | 6.0/7.1 | yes | yes | no 
50 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#10547](https://github.com/wordpress-mobile/WordPress-Android/issues/10547), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 13.3  | Social | 2.3K | 6.0/7.1 | yes | yes | no 
51 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#10363](https://github.com/wordpress-mobile/WordPress-Android/issues/10363), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 13.1  | Social | 2.3K | 6.0/7.1 | yes | yes | no 
52 | *[wordpress](https://github.com/wordpress-mobile/WordPress-Android)* | [#10302](https://github.com/wordpress-mobile/WordPress-Android/issues/10302), [data](https://github.com/the-themis-benchmarks/home/tree/master/WordPress) | 12.9  | Social | 2.3K | 6.0/7.1 | yes | yes | no 


## Themis's Infrastructure

Themis contains a unified, extensible infrastructure for benchmarking automated GUI testing
for Android. Any testing tools can be easily integrated into this infrastructure and
deployed on a given machine with one line of command. 


### List of Supported Tools 
Tool Name | Venue | Open-source | Main Technique | Need App Code? | Need App Instrumentation | Supported SDKs | Implementation Basis 
--- | --- | --- | --- | --- | --- | --- | --- | 
Monkey | - | yes | Random Testing | no | no | Any | -
[Ape](https://github.com/tianxiaogu/ape) | ICSE'19 | yes | Model-based | no | no | 6.0/7.1 | Monkey-based
[Humanoid](https://github.com/yzygitzh/Humanoid) | ASE'19 | yes | Deep learning-based | no | no | Any | DroidBot-based
[ComboDroid](https://github.com/skull591/ComboDroid-Artifact) | ICSE'20 | yes | Model-based | no | yes | 6.0/7.1 | Monkey-based
[TimeMachine](https://github.com/DroidTest/TimeMachine) | ICSE'20 | yes | State-based | no | yes | 4.4/7.1 | Monkey-based
[Q-testing](https://github.com/anlalalu/Q-testing) | ISSTA'20 | no | reinforcement learning-based | no | no | 4.4/7.1/9.0 | -
[Stoat](https://github.com/tingsu/Stoat) | FSE'17 | yes | Model-based | no | no | Any | A3E-based 
[Sapienz](https://github.com/Rhapsod/sapienz) | ISSTA'16 | no | Search-based | no | no | 4.4 | Monkey-based
 

### The command line of deployment:
```
usage: themis.py [-h] [--avd AVD_NAME] [--apk APK] [-n NUMBER_OF_DEVICES]
                [--apk-list APK_LIST] -o O [--time TIME] [--repeat REPEAT]
                [--max-emu MAX_EMU] [--no-headless] [--login LOGIN_SCRIPT]
                [--wait IDLE_TIME] [--monkey] [--ape] [--timemachine]
                [--combo] [--combo-login] [--humandroid] [--stoat] [--sapienz]
                [--offset OFFSET]

optional arguments:
  -h, --help            show this help message and exit
  --avd AVD_NAME
  --apk APK
  -n NUMBER_OF_DEVICES  number of available emulators for testing
  --apk-list APK_LIST   list of apks under test
  -o O                  output dir
  --time TIME           the fuzzing time in hours (e.g., 6h), minutes (e.g.,
                        6m), or seconds (e.g., 6s), default: 6h
  --repeat REPEAT       the repeated number of runs
  --max-emu MAX_EMU     the maximum allowed number of emulators
  --no-headless         show gui
  --login LOGIN_SCRIPT  the script for login
  --wait IDLE_TIME      the idle time to wait before starting the fuzzing
  --monkey
  --ape
  --timemachine
  --combo
  --combo-login
  --humandroid
  --qtesting
  --stoat
  --sapienz
  --offset OFFSET       device offset number
```

-----------

Implementation details
----------------------

The directory structure of Themis is as follows:

    Themis
       |
       |--- scripts:                    scripts for running testing tools and analyzing testing results.
           |
           |--- themis.py:              the main script for deploying themis.
           |
           |--- check_crash.py:         the script to check whether a tool find the bugs.
           |
           |--- compute_coverage.py:    the script to compute the code coverage achieved by a tool.
           |
           |--- compare_bug_triggering_time.py: the script to pairwisely compare bug-triggering times between different tools.          
           |
       |--- tools:                       the supported auotmated testing tools.
           |
           |--- Humanoid
           |
           |--- TimeMachine
           |
           |--- Q-testing
           |
           |--- Ape
           |
           |--- ComboDroid
           |
           |--- Monkey
           |
       |--- app_1:             The bugs collected from app_1.
       |
       |--- app_2:             The bugs collected from app_2.
       |
       |--- ...
       |
       |--- app_N              The bugs collected from app_n.

# 1. Getting Started

## 1.1 Running Themis in Virtual Machine

You can download the Themis package `Themis_VM.zip` from [this link]() on Google Drive (publicly accessible).

### Requirements

* You need to enable the virtualization technology in your computer's BIOS (see [this link](https://stackoverflow.com/questions/35456063/enable-intel-vt-x-intel-virtualization-technology-intel-vt-x) for how to enable the virtualization technology). Most computers by default have this virtualization option turned on. 
* Your computer needs at least 16G of memory, and at least 40G of storage.
* We built our artifact by using VirtualBox [v6.1.20](). After installing virtualbox, you may need to reboot the computer.

### Setting up

1. Extract the downloaded file `Themis_VM.zip` and get the VM image file `Themis.ova`.
2. Open VirtualBox, click "File", click "Import Appliance", then import the file named `Themis.ova` (this step may take about five to ten minutes to complete). 
3. After the import is completed, you should see "vm" as one of the listed VMs in your VirtualBox.
4. Click "Settings", click "System", click "Processor", and check "Enable Nested VT-x/AMD-V"
5. Run the virtual machine. The username and the password are both `Themis`.
6. If you could not run the VM with "Nested VT-x/AMD-V" option enabled in VirtualBox, you should check whether the Hyper-V option is enabled. You can disable the Hyper-V option (see [this link](https://forums.virtualbox.org/viewtopic.php?f=1&t=62339) for more information about this).

### Run

1. switch to Themis's scripts directory

```
cd themis/scripts
```

2. run a testing tool on a target bug

```
python3 themis.py --avd avd_Android7.1 --apk ../commons/commons-2.11.0-#3244.apk -n 1 --repeat 3 --time 1h -o ../monkey-results/ --login ../commons/login-2.11.0-#3244.py --monkey --offset 1
```

Here, 
* `--avd avd_Android7.1` specifies the emulator for running 
* `--apk ../commons/commons-2.11.0-#3244.apk` specifies the target bug is from `commons`'s bug #3244 (v2.11.0) 
* `-n 1` denotes only one emulator instance will be created
* `--repeat 3` denotes the testing process will be repeated for 3 rounds
* `--time 1h` allocates 1 hour for one round of testing
* `-o ../monkey-results/` specifies the output directory of testing results
* `--login ../commons/login-2.11.0-#3244.py` specifies the login script (which will be executed before GUI testing) if the app requires user credentials
* `--monkey` specifies the testing tool
* `--offset 1` indicates the emulator's serial starts from `emulator-5556` (Android emulators' serials start from `emulator-5554` and end at `emulator-5584`, and by default 16 emulators at most are allowed to run in parallel on one native machine)

3. inspect the output files


## 1.2 Setup Themis from scratch 

In practice, we recommend the users to setup our artifact on native machines rather than virtual machines to ensure the optimal testing performance. Thus, we provide the instructions to setup Themis from scratch.

1. setup Android development environment on your local native machine

2. create an Android emulator before running Themis (see [this link](https://stackoverflow.com/questions/43275238/how-to-set-system-images-path-when-creating-an-android-avd) for creating an emulator using [avdmanager](https://developer.android.com/studio/command-line/avdmanager)).

- An example: create an Android emulator ``avd_Android7.1`` with SDK version 7.1 (API level 25), X86 ABI image and Google APIs: 
```
sdkmanager "system-images;android-25;google_apis;x86"
avdmanager create avd --force --name avd_Android7.1 --package 'system-images;android-25;google_apis;x86' --abi google_apis/x86 --sdcard 1024M --device 'Nexus 7'
```
3. (optional) modify the emulator configuration to ensure optimal testing performance of testing tools (config.ini): 

- Here, we set an emulator with 2GB RAM, 1GB SdCard, 1GB internal storage and 256MB heap size.

```
sdcard.size=1024M
disk.dataPartition.size=1024M
vm.heapSize=256
hw.ramSize=2048
``` 

4. (optional but recommended) copy dummy documents into emulators to allow file access from the apps under test

```
emulator -avd avd_Android7.1 -port 5554 &
cd themis/scripts
bash -x copy_dummy_documents.sh emulator-5554
emu kill emulator-5554
```

5. install [uiautomator2](https://github.com/openatx/uiautomator2), which is used for executing login scripts

```
pip3 install --upgrade --pre uiautomator2
```

