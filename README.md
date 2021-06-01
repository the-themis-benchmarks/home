# The Themis Benchmark

Themis is a collection of real-world, reproducible crash bugs (collected from 
open-source Android apps) and a unified, extensible infrastructure 
for benchmarking automated GUI testing for Android and beyond. 

# 1. Contents of Themis

## Themis's bug dataset

Themis now contains *52* reproducible crash bugs. All these bugs are labeled by
the app developers as "critical bugs" (i.e., important bugs), which affected the 
major app functionalities and the larger percentage of app users.

For each bug, we provide:

- The original bug report of the bug

- An executable APK (Jacoco-instrumented for coverage collection),
 
- A bug-reproducing script (python-based script for bug inspection) and a video 

- The stack trace of the bug 

- Metadata for supporting evaluation (e.g., bug explanation, login script, configuration files used by the Themis's infrastructure)

- the app source code w.r.t each bug 


### List of crash bugs
Issue Id | App | Bug report, data | Version | Category | GitHub Stars | Reproducible? | Network? | Login? | System Setting? 
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
[Monkey](https://developer.android.com/studio/test/monkey?hl=en) | - | yes | Random Testing | no | no | Any | -
[Ape](https://github.com/tianxiaogu/ape) | ICSE'19 | yes | Model-based | no | no | 6.0/7.1 | Monkey-based
[Humanoid](https://github.com/yzygitzh/Humanoid) | ASE'19 | yes | Deep learning-based | no | no | Any | DroidBot-based
[ComboDroid](https://github.com/skull591/ComboDroid-Artifact) | ICSE'20 | yes | Model-based | no | yes | 6.0/7.1 | Monkey-based
[TimeMachine](https://github.com/DroidTest/TimeMachine) | ICSE'20 | yes | State-based | no | yes | 4.4/7.1 | Monkey-based
[Q-testing](https://github.com/anlalalu/Q-testing) | ISSTA'20 | no | reinforcement learning-based | no | no | 4.4/7.1/9.0 | -
[Stoat](https://github.com/tingsu/Stoat) | FSE'17 | yes | Model-based | no | no | Any | A3E-based 
[Sapienz](https://github.com/Rhapsod/sapienz) | ISSTA'16 | no | Search-based | no | no | 4.4 | Monkey-based
 

### The command line for deployment:

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

### Implementation details

The directory structure of Themis is as follows:

    Themis
       |
       |--- esecfse2021-paper1009.pdf   the accepted paper of Themis
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
           |--- run_monkey.sh           the internal shell script to invokte Monkey, Ape, Humanoid, ComboDroid, TimeMachine and Q-testing
           |--- run_ape.sh
           |--- run_humanoid.sh
           |--- run_qtesting.sh
           |--- run_timemachine.sh
           |--- run_combodroid.sh
           |
       |--- tools:                      the supported auotmated testing tools.
           |
           |--- Humanoid                the tool Humanoid 
           |
           |--- TimeMachine             the tool TimeMachine
           | 
           |--- Q-testing               the tool Q-testing
           |
           |--- Ape                     the tool Ape
           |
           |--- ComboDroid              the tool ComboDroid
           |
           |--- Monkey                  the tool Monkey
           |
       |--- app_1:             The bugs collected from app_1.
       |
       |--- app_2:             The bugs collected from app_2.
       |
       |--- ...
       |
       |--- app_N              The bugs collected from app_n.

# 2. Instructions for Artifact Evaluation

For artifact evaluation, we recommend you to run Themis in Virtual Machine. All the required stuffs are already installed and prepared. You can download the VM package `Themis_VM.zip` from [this link]() on Google Drive (fully-anonymized and publicly accessible).

## Prerequisite

* You need to enable the virtualization technology in your computer's BIOS (see [this link](https://stackoverflow.com/questions/35456063/enable-intel-vt-x-intel-virtualization-technology-intel-vt-x) for how to enable the virtualization technology). Most computers by default already have this virtualization option turned on. 
* Your computer needs at least 16G of memory, and at least 40G of storage.
* We built our artifact by using VirtualBox [v6.1.20](https://www.virtualbox.org/wiki/Download_Old_Builds_6_1). Please install VirtualBox based on your OS type. After installing VirtualBox, you may need to reboot the computer. 

## Setup Virtual Machine

1. Extract the downloaded file `Themis_VM.zip` and get the VM image file `Themis.ova`.
2. Open VirtualBox, click "File", click "Import Appliance", then import the file named `Themis.ova` (this step may take about five to ten minutes to complete). 
3. After the import is completed, you should see "vm" as one of the listed VMs in your VirtualBox.
4. Click "Settings", click "System", click "Processor", and check "Enable Nested VT-x/AMD-V"
5. Run the virtual machine. The username and the password are both `Themis`.
6. If you could not run the VM with "Nested VT-x/AMD-V" option enabled in VirtualBox, you should check whether the Hyper-V option is enabled. You can disable the Hyper-V option (see [this link](https://forums.virtualbox.org/viewtopic.php?f=1&t=62339) for more information about this).

## Getting Started (for Initial Review)

Take the quick test to get familar with Themis and validate whether it is ready for evaluation.

**Step 1. open a terminal and switch to Themis's scripts directory**

```
cd themis/scripts
```

**Step 2. run Monkey on one target bug**

```
python3 themis.py --no-headless --avd Android7.1 --apk ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk --time 10m -o ../monkey-results/ --monkey
```

Here, 
* `--no-headless` shows the emulator GUI. 
* `--avd Android7.1` specifies the name of the emulator (which has already been created in the VM).
* `--apk ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk` specifies the target bug which is `ActivityDiary`'s bug `#118` in `v1.1.8`.
* `--time 10m` allocates 10 minutes for the testing tool to find the bug 
* `-o ../monkey-results/` specifies the output directory of testing results
* `--monkey` specifies the testing tool

*Expected results:* you should see (1) an Android emulator is started, (2) the app `ActivityDiary` is installed and started, (3) Monkey is started to test the app, (4) the following sample texts are outputted on the terminal during testing, and (5) the emulator is automatically closed at the end.

<details>
<summary>**click to see the sample output on the terminal of a successful run.**</summary>
<pre><code>
allocate emulators: emulator-5554
the apk list to fuzz: ['../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk']
True
Now allocate the apk: ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk on emulator-5554
its login script: ""
wait the allocated devices to finish...
execute monkey: bash -x run_monkey.sh ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk emulator-5554 Android7.1 ../monkey-results/ 10m "" ""
+ APK_FILE=../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk
+ AVD_SERIAL=emulator-5554
+ AVD_NAME=Android7.1
+ OUTPUT_DIR=../monkey-results/
+ TEST_TIME=0.5m
+ HEADLESS=
+ LOGIN_SCRIPT=
+ RETRY_TIMES=5
++ seq 1 5
+ for i in $(seq 1 $RETRY_TIMES)
+ echo 'try to start the emulator (emulator-5554)...'
try to start the emulator (emulator-5554)...
+ sleep 5
+ avd_port=5554
+ sleep 5
+ emulator -port 5554 -avd Android7.1 -read-only
emulator: Requested console port 5554: Inferring adb port 5555.
qemu-system-i386: warning: TSC frequency mismatch between VM (2903985 kHz) and host (2903991 kHz), and TSC scaling unavailable
qemu-system-i386: warning: TSC frequency mismatch between VM (2903985 kHz) and host (2903991 kHz), and TSC scaling unavailable
+ wait_for_device emulator-5554
+ avd_serial=emulator-5554
+ timeout 5s adb -s emulator-5554 wait-for-device
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ i=0
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#0 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#0 times) ...
+ sleep 5
++ expr 0 + 1
+ i=1
+ [[ 1 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#1 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#1 times) ...
+ sleep 5
++ expr 1 + 1
+ i=2
+ [[ 2 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#2 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#2 times) ...
+ sleep 5
++ expr 2 + 1
+ i=3
+ [[ 3 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#3 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#3 times) ...
+ sleep 5
++ expr 3 + 1
+ i=4
+ [[ 4 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#4 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#4 times) ...
+ sleep 5
++ expr 4 + 1
+ i=5
+ [[ 5 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#5 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#5 times) ...
+ sleep 5
++ expr 5 + 1
+ i=6
+ [[ 6 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#6 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#6 times) ...
+ sleep 5
++ expr 6 + 1
+ i=7
+ [[ 7 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#7 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#7 times) ...
+ sleep 5
++ expr 7 + 1
+ i=8
+ [[ 8 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#8 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#8 times) ...
+ sleep 5
++ expr 8 + 1
+ i=9
+ [[ 9 == 10 ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ echo '   Waiting for emulator (emulator-5554) to fully boot (#9 times) ...'
   Waiting for emulator (emulator-5554) to fully boot (#9 times) ...
+ sleep 5
++ expr 9 + 1
+ i=10
+ [[ 10 == 10 ]]
+ echo 'Cannot connect to the device: (emulator-5554) after (#10 times)...'
Cannot connect to the device: (emulator-5554) after (#10 times)...
+ break
++ adb -s emulator-5554 shell getprop init.svc.bootanim
adb: device offline
+ OUT=
+ [[ '' != \s\t\o\p\p\e\d ]]
+ adb -s emulator-5554 emu kill
OK: killing emulator, bye bye
OK
+ echo 'try to restart the emulator (emulator-5554)...'
try to restart the emulator (emulator-5554)...
+ [[ 10 == RETRY_TIMES ]]
+ for i in $(seq 1 $RETRY_TIMES)
+ echo 'try to start the emulator (emulator-5554)...'
try to start the emulator (emulator-5554)...
+ sleep 5
emulator: WARNING: Not saving state: RAM not mapped as shared
+ avd_port=5554
+ sleep 5
+ emulator -port 5554 -avd Android7.1 -read-only
emulator: Requested console port 5554: Inferring adb port 5555.
qemu-system-i386: warning: TSC frequency mismatch between VM (2903985 kHz) and host (2903991 kHz), and TSC scaling unavailable
qemu-system-i386: warning: TSC frequency mismatch between VM (2903985 kHz) and host (2903991 kHz), and TSC scaling unavailable
+ wait_for_device emulator-5554
+ avd_serial=emulator-5554
+ timeout 5s adb -s emulator-5554 wait-for-device
++ adb -s emulator-5554 shell getprop init.svc.bootanim
+ OUT=stopped
+ i=0
+ [[ stopped != \s\t\o\p\p\e\d ]]
++ adb -s emulator-5554 shell getprop init.svc.bootanim
+ OUT=stopped
+ [[ stopped != \s\t\o\p\p\e\d ]]
+ break
+ echo '  emulator (emulator-5554) is booted!'
  emulator (emulator-5554) is booted!
+ adb -s emulator-5554 root
restarting adbd as root
++ date +%Y-%m-%d-%H-%M-%S
+ current_date_time=2021-05-26-16-58-44
++ basename ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk
+ apk_file_name=ActivityDiary-1.1.8-debug-#118.apk
+ result_dir=../monkey-results//ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2021-05-26-16-58-44
+ mkdir -p ../monkey-results//ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2021-05-26-16-58-44
+ echo '** CREATING RESULT DIR (emulator-5554): ' ../monkey-results//ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2021-05-26-16-58-44
** CREATING RESULT DIR (emulator-5554):  ../monkey-results//ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2021-05-26-16-58-44
+ [[ '' != '' ]]
+ adb -s emulator-5554 install -g ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk
+ echo '** INSTALL APP (emulator-5554)'
** INSTALL APP (emulator-5554)
+ sleep 10
++ aapt dump badging ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk
++ grep package
++ awk '{print $2}'
++ sed s/name=//g
++ sed 's/'\''//g'
+ app_package_name=de.rampro.activitydiary.debug
+ echo '** PROCESSING APP (emulator-5554): ' de.rampro.activitydiary.debug
** PROCESSING APP (emulator-5554):  de.rampro.activitydiary.debug
+ echo '** START LOGCAT (emulator-5554) '
** START LOGCAT (emulator-5554) 
+ adb -s emulator-5554 logcat -c
+ echo '** START COVERAGE (emulator-5554) '
** START COVERAGE (emulator-5554) 
+ adb -s emulator-5554 logcat AndroidRuntime:E CrashAnrDetector:D System.err:W CustomActivityOnCrash:E ACRA:E WordPress-EDITOR:E '*:F' '*:S'
+ echo '** RUN MONKEY (emulator-5554)'
** RUN MONKEY (emulator-5554)
+ adb -s emulator-5554 shell date +%Y-%m-%d-%H:%M:%S
+ bash dump_coverage.sh emulator-5554 de.rampro.activitydiary.debug ../monkey-results//ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2021-05-26-16-58-44
+ timeout 10m adb -s emulator-5554 shell monkey -p de.rampro.activitydiary.debug -v --throttle 200 --ignore-crashes --ignore-timeouts --ignore-security-exceptions --bugreport 1000000
+ tee ../monkey-results//ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2021-05-26-16-58-44/monkey.log
:Monkey: seed=1622177363949 count=1000000
:AllowPackage: de.rampro.activitydiary.debug
:IncludeCategory: android.intent.category.LAUNCHER
:IncludeCategory: android.intent.category.MONKEY
// Event percentages:
//   0: 15.0%
//   1: 10.0%
//   2: 2.0%
//   3: 15.0%
//   4: -0.0%
//   5: -0.0%
//   6: 25.0%
//   7: 15.0%
//   8: 2.0%
//   9: 2.0%
//   10: 1.0%
//   11: 13.0%
:Switch: #Intent;action=android.intent.action.MAIN;category=android.intent.category.LAUNCHER;launchFlags=0x10200000;component=de.rampro.activitydiary.debug/de.rampro.activitydiary.ui.main.MainActivity;end
    // Allowing start of Intent { act=android.intent.action.MAIN cat=[android.intent.category.LAUNCHER] cmp=de.rampro.activitydiary.debug/de.rampro.activitydiary.ui.main.MainActivity } in package de.rampro.activitydiary.debug
:Sending Trackball (ACTION_MOVE): 0:(3.0,0.0)
:Sending Touch (ACTION_DOWN): 0:(6.0,111.0)
:Sending Touch (ACTION_UP): 0:(75.08969,0.25681877)
:Sending Touch (ACTION_DOWN): 0:(461.0,414.0)
:Sending Touch (ACTION_UP): 0:(463.19458,413.57645)
:Sending Touch (ACTION_DOWN): 0:(443.0,1154.0)
:Sending Touch (ACTION_UP): 0:(337.0955,1190.089)
:Sending Touch (ACTION_DOWN): 0:(392.0,379.0)
:Sending Touch (ACTION_UP): 0:(404.1744,297.83728)
:Sending Trackball (ACTION_MOVE): 0:(-1.0,-4.0)
:Sending Touch (ACTION_DOWN): 0:(739.0,89.0)
:Sending Touch (ACTION_UP): 0:(800.0,146.10786)
:Sending Trackball (ACTION_MOVE): 0:(-3.0,4.0)
:Sending Touch (ACTION_DOWN): 0:(749.0,443.0)
:Sending Touch (ACTION_UP): 0:(747.92065,456.49356)
:Sending Touch (ACTION_DOWN): 0:(485.0,814.0)
:Sending Touch (ACTION_UP): 0:(492.87933,804.6225)
:Sending Trackball (ACTION_MOVE): 0:(-4.0,-4.0)
:Sending Trackball (ACTION_MOVE): 0:(0.0,2.0)
:Sending Touch (ACTION_DOWN): 0:(454.0,119.0)
:Sending Touch (ACTION_UP): 0:(465.00302,121.41099)
:Sending Touch (ACTION_DOWN): 0:(476.0,305.0)
:Sending Touch (ACTION_UP): 0:(476.1956,313.51404)
+ adb -s emulator-5554 shell date +%Y-%m-%d-%H:%M:%S
+ echo '** STOP MONKEY (emulator-5554)'
** STOP MONKEY (emulator-5554)
++ adb -s emulator-5554 shell ps
++ grep monkey
++ awk '{print $2}'
+ adb -s emulator-5554 shell kill 17521
+ echo '** STOP COVERAGE (emulator-5554)'
** STOP COVERAGE (emulator-5554)
++ ps aux
++ grep 'dump_coverage.sh emulator-5554'
++ grep -v grep
++ awk '{print $2}'
+ kill 1248836
+ echo '** STOP LOGCAT (emulator-5554)'
** STOP LOGCAT (emulator-5554)
++ ps aux
++ grep 'emulator-5554 logcat'
++ grep -v grep
++ awk '{print $2}'
+ kill 1248835
+ sleep 5
+ adb -s emulator-5554 emu kill
OK: killing emulator, bye bye
OK
+ echo '@@@@@@ Finish (emulator-5554): ' de.rampro.activitydiary.debug @@@@@@@
@@@@@@ Finish (emulator-5554):  de.rampro.activitydiary.debug @@@@@@@
</code></pre>
</details>

**Step 3. inspect the output files**

If Step 2 succeeds, you can see the outputs under `../monkey-results/` (i.e., `themis/monkey-results/`). 

```
$ cd ../monkey-results/
$ ls
  ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2020-06-24-20:39:27/         # the output directory
$ cd ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2020-06-24-20:39:27/
$ ls
  coverage_1.ec   # the coverage data file  (used for computing coverage)
  coverage_2.ec 
  install.log     # the log of app installation
  logcat.log      # the system log of emulator (this file contains the crash stack traces if the target bug was triggered)
  monkey.log      # the log of Monkey (including the events that Monkey generates)
  monkey_testing_time_on_emulator.txt  # the first line is the starting testing time, and the second line is the ending testing time
```

If you can see all these files and these files are non-empty (use `ls -l` to check), the quick test succeeds. Note that the number of coverage files varies according to the testing time. In practice, Themis notifies an app to dump coverage data every five minutes.



## Whole Evaluation (for In-depth Review)

**1. Validate the supported tools (Table 2 in the accepted paper)**

Themis now supports and maintains 6 state-of-the-art fully-automated testing tools for Android (see below). These tools can be cloned from Themis's repositories and are put under `themis/tools`.

* `Monkey`: distributed with Android SDKs
* `Ape`: https://github.com/the-themis-benchmarks/Ape-bin
* `combodroid`: https://github.com/the-themis-benchmarks/combodroid
* `Humanoid`: https://github.com/the-themis-benchmarks/Humanoid
* `Q-testing`: https://github.com/the-themis-benchmarks/Q-testing
* `TimeMachine`: https://github.com/the-themis-benchmarks/TimeMachine

Note that these tools are the modified/enhanced versions of their originals because we coordinated with the authors of these tools to assure correct and rigorous setup (e.g., report the encountered tool bugs to the authors for fixing). We tried our best efforts to minimize the bias and ensure that each tool is at "its best state" in bug finding (see **Section 3.2** in the accepted paper).

Specifically, we track the tool modifications to facilitate review and validation. We spent slight efforts to integrate `Monkey`, `Ape`, `Humanoid` and `Q-testing` into Themis. `Combodroid` was modifled by its author and intergrated into Themis, while `TimeMachine` was modified by us and later verified by its authors (view [this commit](https://github.com/the-themis-benchmarks/TimeMachine/commit/b5bafb28fae26cc0dff2e36599c1af6c166ce48c) to check all the modifications/enhancements made in `TimeMachine`).

**2. Validate the bug dataset (Table 3 in the accepted paper)**

Themis now contains *52* reproducible crash bugs. For each bug, you can view:
* its metadata (e.g., original bug report, buggy app version) 
* its bug data (stack trace, executable apk, bug-triggering script/video) 
* its property (e.g., the minimal number of user actions to reproduce the bug, the Android SDKs on which the bug can be reproduced, does the app require network or login, does the bug involve changing system settings).

**3. Validate the bug finding results of these tools (Table 3, Table 4, Figure 1 in the accepted paper)**

Our original evaluation setup (see **Section 3.3** in the accepted paper) is: 

```
We deployed our experiment on a 64-bit Ubuntu 18.04 machine (64
cores, AMD 2990WX CPU, and 128GB RAM). We chose Android 7.1
emulators (API level 25) since all selected tools support this version.
Each emulator is configured with 2GB RAM, 1GB SDCard, 1GB
internal storage, and X86 ABI image. Different types of external
files (including PNGs/MP3s/PDFs/TXTs/DOCXs) are stored on the
SDCard to facilitate file access from apps.

We allocated one device (i.e., one emulator) for each bug/tool 
in one run (one run required 6 hours), and repeated
5 runs for each bug/tool. The whole evaluation took over
52×5×6×7 = 10,920 machine hours (not including Sapienz). Due to
Android’s limitation, we can only run 16 emulators in parallel on
one physical machine. Thus, the evaluation took us around 28 days,
in addition to around one week for deployment preparation.
```

*Considering the large evaluation cost, we recommend you to try running 1-2 tools on 1-2 bugs at your will to validate
the artifact if you do not have enough resources/time. 
Of course, to allow full validation, we provided all the data files of our evaluation for inspection.
To replicate the whole evaluation, we strongly recommend you to build/use Themis from scratch (detailed in Part 3 of this README) on a local native machine or a server.*

** In the following, we take `Monkey` as a tool and `ActivityDiary-1.1.8-debug-#118.apk` as a target bug to illustrate how to replicate our evaluation. ** 

(1) run `Monkey` on `ActivityDiary-1.1.8-debug-#118.apk` for 6 hours and repeat this process for 5 runs (**this step will take 30 hours to finish because of 5 runs of testing on one emulator**)

```
python3 themis.py --no-headless --avd Android7.1 --apk ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk -n 1 --repeat 5 --time 6h -o ../monkey-results/ --monkey 
```

Here, 
* `--no-headless` shows the emulator GUI 
* `--avd Android7.1` specifies the name of the emulator (which has already been created in the VM).
* `--apk ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk` specifies the target bug which is `ActivityDiary`'s bug `#118` in `v1.1.8`.
* `-n 1` denotes one emulator instance will be created (in practice at most 16 emulators are allowed to run in parallel on one native machine)
* `--repeat 5` denotes the testing process will be repeated for 5 runs (these 5 runs will be distributed to the available emulator instances)
* `--time 6h` allocates 6 hours for the testing tool to find the bug 
* `-o ../monkey-results/` specifies the output directory of testing results
* `--monkey` specifies the testing tool

If you do not have enough resources/time, we recommend you to shorten the testing time (e.g., use `--time 1h` for 1 hour or `--time 30m` for 30 minutes). We recommend you to use only one or two emulators (e.g., `-n 1` for 1 emulator or `-n 2` for 2 emulators) in the VM because of limited memory.

Thus, you can use the following command (**this step will take 2 hours to finish because of 2 runs of testing on one emulator**).

```
python3 themis.py --no-headless --avd Android7.1 --apk ../ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk -n 1 --repeat 2 --time 1h -o ../monkey-results/ --monkey 
```

应该给出明确的instruction，如何验证结果，比如说最后会在对应目录下产生2个输出目录。

(2) When the testing terminates, you can inspect whether the target bug was found or not in each run, how long does it take to find the bug, and how many times the bug was found by using the command below.

```
python3 check_crash.py --monkey -o ../monkey-results/ --app ActivityDiary --id \#118 --simple
```
Here, 
* `--app ActivityDiary` specifies the target app (You can omit this option to check all the tested apps and their bugs).
* `--id \#118` specifies the target bug id (You can omit this option to check all the target bugs of app `ActivityDiary`).
* `--simple` outputs the checking result to the terminal for quick check (You can substitute `--simple` with `--csv FILE_PATH` to output the checking results into a CSV file). 
* Use `-h` to see the detailed list of command options.

An example output could be (In this case, the target bug, `ActivityDiary`'s `#118`, was not found by Moneky in the five runs):

<details>
<summary>**click to see the sample output on the terminal of a successful run.**</summary>
<pre><code>
ActivityDiary


=========


[ActivityDiary, #118] scanning (ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5554.Android7.1#2020-06-24-20:39:27) 
[ActivityDiary, #118] testing time: 2020-06-24-20:39:33 
the start testing time is: 2020-06-24-20:39:33
the start testing time (parsed) is: 2020-06-24 20:39:33


[ActivityDiary, #118] scanning (ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5556.Android7.1#2020-06-24-20:39:32) 
[ActivityDiary, #118] testing time: 2020-06-24-20:39:36 
the start testing time is: 2020-06-24-20:39:36
the start testing time (parsed) is: 2020-06-24 20:39:36


[ActivityDiary, #118] scanning (ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5558.Android7.1#2020-06-24-20:39:37) 
[ActivityDiary, #118] testing time: 2020-06-24-20:39:43 
the start testing time is: 2020-06-24-20:39:43
the start testing time (parsed) is: 2020-06-24 20:39:43


[ActivityDiary, #118] scanning (ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5560.Android7.1#2020-06-24-20:39:42) 
[ActivityDiary, #118] testing time: 2020-06-24-20:39:47 
the start testing time is: 2020-06-24-20:39:47
the start testing time (parsed) is: 2020-06-24 20:39:47


[ActivityDiary, #118] scanning (ActivityDiary-1.1.8-debug-#118.apk.monkey.result.emulator-5562.Android7.1#2020-06-24-20:39:47) 
[ActivityDiary, #118] testing time: 2020-06-24-20:39:52 
the start testing time is: 2020-06-24-20:39:52
the start testing time (parsed) is: 2020-06-24 20:39:52
</code></pre>
</details>

Another example output could be (In this case, the target bug, `AnkiDroid`'s `#4451`, was found by 1 time after running Monkey for 55 minutes in one run):

```
AnkiDroid


=========


[AnkiDroid, #4451] scanning (AnkiDroid-debug-2.7beta1-#4451.apk.monkey.result.emulator-5556.Android7.1#2020-06-26-00:59:33) 
[AnkiDroid, #4451] testing time: 2020-06-26-00:59:34 
[AnkiDroid, #4451] testing time: 2020-06-26-06:59:35 
the start testing time is: 2020-06-26-00:59:34
the start testing time (parsed) is: 2020-06-26 00:59:34
[AnkiDroid, #4451] the crash was triggered (1) times
[AnkiDroid, #4451] the time duration: ['55'] (mins)

```

应该给出明确的instructions验证结果：通过检查发现2次运行，monkey对ActivityDiary，一次也没找到，对应到Table 3中就没有×，对应的Table4中就是 0/5; monkey对AnkiDroid又是另外一个情况。然后联系具体的文件。

### Notes

(1) you can substitute `--monkey` with `--ape`, `--combo`, `--humandroid`,  `--qtesting` or `--timemachine` to try the corresponding tool. You also need to change the output directory `-o ../monkey-results/` to a distinct directory, e.g., `-o ../ape-results`. You can follow the similar steps described above to inspect whether the target bug was found or not and the related info.


(2) If the app under test requires user login, you should specify the login script. Themis will call the login script before testing. For example, if we run `Monkey` on `../commons/commons-2.11.0-#3244.apk` which requires user login, the command line should be:

```
python3 themis.py --avd Android7.1 --apk ../commons/commons-2.11.0-#3244.apk -n 1 --repeat 5 --time 6h -o ../monkey-results/ --login ../commons/login-2.11.0-#3244.py --monkey 
```

Here, 
* `--login ../commons/login-2.11.0-#3244.py` specifies the login script (which will be executed before GUI testing) 


**3. validate the data files**


# 3. Instructions for Reusing Themis

## Build and Use Themis from Scratch

In practice, we *strongly recommend* the users to setup our artifact on local native machines or remote servers rather than virtual machines to ensure (1) the optimal testing performance and (2) evaluation efficiency. Thus, we provide the instructions to setup Themis from scratch.

1. setup Android development environment and `Python 3` on your machine 

2. create an Android emulator before running Themis (see [this link](https://stackoverflow.com/questions/43275238/how-to-set-system-images-path-when-creating-an-android-avd) for creating an emulator using [avdmanager](https://developer.android.com/studio/command-line/avdmanager)).

- An example: create an Android emulator ``avd_Android7.1`` with SDK version 7.1 (API level 25), X86 ABI image and Google APIs: 
```
sdkmanager "system-images;android-25;google_apis;x86"
avdmanager create avd --force --name avd_Android7.1 --package 'system-images;android-25;google_apis;x86' --abi google_apis/x86 --sdcard 1024M --device 'Nexus 7'
```
3. (optional) modify the emulator configuration to ensure optimal testing performance of testing tools: 

In our evaluation, we set an emulator with 2GB RAM, 1GB SdCard, 1GB internal storage and 256MB heap size.

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

6. If you run Themis on remote servers, please omit the option `--no-headless` which turns off the emulator GUI.


7. Install all the necessary dependecies required by the respective testing tools.

## Extend Themis for Future Research

1. Add new crash bugs into Themis

Take `ActivityDiary-1.1.8-debug-#118.apk` as an example, the basic steps to add such a bug into Themis's dataset include:
* build the buggy app version into an executable apk file (i.e., `ActivityDiary/ActivityDiary-1.1.8-debug-#118.apk`, where `ActivityDiary` is the app name, `1.1.8` is the code version, `#118` is the original issue id.)
* reproduce the bug and record the stack trace (i.e., `ActivityDiary/crash_stack_#118.txt`)
* write a bug-triggering script in `uiautomator2` and record a bug-triggering video (i.e., `ActivityDiary/script-#118.py` and `ActivityDiary/video-#118.mp4`)
* add a JSON file to facilitate coverage computation (used by `TimeMachine`) which describes its class files and source files (i.e., `ActivityDiary/class_files.json`)

The basic steps to add such a bug into Themis's infrastructure include:
* In `scripts/check_crash.py`, one should add the app name into list `ALL_APPS` and the crash signature (i.e., the crash type info and the partial crash trace  related to the app itself) into dict `app_crash_data`.

*In the future, we plan to (1) add the crash bugs from other existing benchmarks, (2) add crash bugs with different levels of severity rather than only critical ones, and (3) add non-crashing bugs (e.g., UI bugs) into Themis. For non-crashing bugs, we can manually codify the bug-triggering condition into specific assertions in the app code so that Themis can be reused to evaluate the existing tools on finding non-crashing bugs by violating the assertions. We are already working on (2).*

2. Add new testing tools into Themis

Take `Monkey` as an example, the basic steps to add a new tool into Themis's infrastructure include:
* add an internal shell script to invoke the new tool (see `scripts/run_monkey.sh`) which defines (1) the concrete command line of invoking the tool, (2) the outputs of the tool, and (3) the tool-specific configurations before running
* add the call of this shell script in `scripts/themis.py` (see function `run_monkey`)
* add the code of parsing the outputs of the new tool in `scripts/check_crash.py`.

In fact, we already have integrated [FastBot](https://github.com/bytedance/Fastbot_Android), an industrial testing tool from ByteDance, into Themis. 

3. Optimize and enhance existing supported tools

In the accepted paper, **Section 4.2 and 4.3** point out many optimization opportunities and future research for improving existing testing tools. By using Themis, 

* The tool authors or other researchers can debug/validate the tool improvement and evaluate/compare with new testing tools 
* We can contribute new enhancement features to the original tools by pull requests because Themis forked the testing tools from their original repositories.

4. Coverage profiling and analysis

Themis now supports coverage profiling by running

```
python3 compute_coverage.py -o ../monkey-results --monkey --app ActivityDiary --id \#118 --acc_csv
```

The main usage is:

```
usage: compute_coverage.py [-h] -o O [-v] [--monkey] [--ape] [--timemachine] [--combo] [--humandroid] [--qtesting] [--stoat] [--app APP_NAME] [--id ISSUE_ID] [--acc_csv ACC_CSV] [--single_csv SINGLE_CSV]
                           [--average_csv AVERAGE_CSV]

optional arguments:
  -h, --help            show this help message and exit
  -o O                  the output directory of testing results
  -v
  --monkey
  --ape
  --timemachine
  --combo
  --humandroid
  --qtesting
  --app APP_NAME
  --id ISSUE_ID
  --acc_csv ACC_CSV     compute the accumulative coverage of all runs
  --single_csv SINGLE_CSV
                        compute the coverage of single runs
  --average_csv AVERAGE_CSV
                        compute the average coverage of all runs
```

5. Themis can also benefit other research (e.g., fault localization, program repair, etc.)

