import os
import time
from argparse import ArgumentParser, Namespace
from multiprocessing.pool import ThreadPool


def get_time_in_seconds(testing_time):
    if 'h' in testing_time:
        testing_time_in_secs = int(testing_time[:-1]) * 60 * 60
    elif 'm' in testing_time:
        testing_time_in_secs = int(testing_time[:-1]) * 60
    elif 's' in testing_time:
        testing_time_in_secs = int(testing_time[:-1])
    else:
        print("Warning: the given time is ZERO seconds!!")
        testing_time_in_secs = 0  # error!

    return testing_time_in_secs


def run_monkey(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script,is_snapshot):
    command = 'bash -x run_monkey.sh %s %s %s %s %s %s %s %s' % (apk, avd_serial, avd_name,
                                                              output_dir,
                                                              testing_time,
                                                              screen_option,
                                                              login_script,
                                                              is_snapshot)
    print('execute monkey: %s' % command)
    os.system(command)


def run_ape(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script,is_snapshot):
    command = 'bash run_ape.sh %s %s %s %s %s %s %s %s' % (apk, avd_serial, avd_name,
                                                        output_dir,
                                                        testing_time,
                                                        screen_option,
                                                        login_script,
                                                        is_snapshot)
    print('execute ape: %s' % command)
    os.system(command)


def run_combodroid(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script):
    command = 'bash -x run_combodroid.sh %s %s %s %s %s %s %s' % (apk, avd_serial, avd_name,
                                                                  output_dir,
                                                                  testing_time,
                                                                  screen_option,
                                                                  login_script)
    print('execute combodroid: %s' % command)
    os.system(command)


def run_combodroid_login(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_combodroid_login.sh %s %s %s %s %s %s %s %s' % (apk, avd_serial, avd_name,
                                                                        output_dir,
                                                                        testing_time,
                                                                        screen_option,
                                                                        login_script,
                                                                        is_snapshot)
    print('execute combodroid with login: %s' % command)
    os.system(command)


def run_timemachine(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, adb_port):
    testing_time_in_secs = get_time_in_seconds(testing_time)

    command = 'bash run_timemachine.sh %s %s %s %s %s %s %s %s' % (apk, avd_serial, avd_name,
                                                                   output_dir,
                                                                   testing_time_in_secs,
                                                                   screen_option,
                                                                   login_script,
                                                                   adb_port)
    print('execute timemachine: %s' % command)
    os.system(command)


def run_humanoid(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script):
    command = 'bash -x run_humanoid.sh %s %s %s %s %s %s %s' % (apk, avd_serial, avd_name,
                                                                output_dir,
                                                                testing_time,
                                                                screen_option,
                                                                login_script)
    print('execute humanoid: %s' % command)
    os.system(command)

def run_droidbot(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script):
    command = 'bash -x run_droidbot.sh %s %s %s %s %s %s %s' % (apk, avd_serial, avd_name,
                                                                output_dir,
                                                                testing_time,
                                                                screen_option,
                                                                login_script)
    print('execute droidbot: %s' % command)
    os.system(command)

def run_weighted(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_weighted.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                             os.path.abspath(output_dir),
                                                             testing_time,
                                                             screen_option,
                                                             login_script,
                                                             is_snapshot)
    print('execute weighted exploration: %s' % command)
    os.system(command)


def run_stoat(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_stoat.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                             os.path.abspath(output_dir),
                                                             testing_time,
                                                             screen_option,
                                                             login_script,
                                                             is_snapshot)
    print('execute stoat: %s' % command)
    os.system(command)


def run_sapienz(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_sapienz.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                               os.path.abspath(output_dir),
                                                               testing_time,
                                                               screen_option,
                                                               login_script,
                                                               is_snapshot)
    print('execute sapienz: %s' % command)
    os.system(command)


def run_qtesting(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_qtesting.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                                os.path.abspath(output_dir),
                                                                testing_time,
                                                                screen_option,
                                                                login_script,
                                                                is_snapshot)
    print('execute Q-testing: %s' % command)
    os.system(command)


def run_fastbot(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_fastbot.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                                  os.path.abspath(output_dir),
                                                                  testing_time,
                                                                  screen_option,
                                                                  login_script,
                                                                  is_snapshot)
    print('execute fastbot: %s' % command)
    os.system(command)


def run_newmonkey(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_newmonkey.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                                    os.path.abspath(output_dir),
                                                                    testing_time,
                                                                    screen_option,
                                                                    login_script,
                                                                    is_snapshot)
    print('execute newmonkey: %s' % command)
    os.system(command)


def run_wetest(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_wetest.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                                 os.path.abspath(output_dir),
                                                                 testing_time,
                                                                 screen_option,
                                                                 login_script,
                                                                 is_snapshot)
    print('execute wetest: %s' % command)
    os.system(command)


def run_fastbot_new(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_fastbot_new.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                                  os.path.abspath(output_dir),
                                                                  testing_time,
                                                                  screen_option,
                                                                  login_script,
                                                                  is_snapshot)
    print('execute fastbot_new: %s' % command)
    os.system(command)


def run_wetest_new(apk, avd_serial, avd_name, output_dir, testing_time, screen_option, login_script, is_snapshot):
    command = 'bash -x run_wetest_new.sh %s %s %s %s %s %s %s %s' % (os.path.abspath(apk), avd_serial, avd_name,
                                                                 os.path.abspath(output_dir),
                                                                 testing_time,
                                                                 screen_option,
                                                                 login_script,
                                                                 is_snapshot)
    print('execute wetest_new: %s' % command)
    os.system(command)


def get_all_apks(apk_list_file):
    file = open(apk_list_file, 'r')
    apk_paths = []
    apk_login_scripts = []
    for line in file.readlines():
        if line.strip().startswith('#'):
            # skip commented apk files
            continue
        if "," in line:
            content = line.split(",")
            apk_paths.append(content[0].strip())
            apk_login_scripts.append(content[1].strip())
        else:
            apk_path = line.strip()
            apk_paths.append(apk_path)
            apk_login_scripts.append("\"\"")
    print("Total %s apks under test" % len(apk_paths))
    return apk_paths, apk_login_scripts


def main(args: Namespace):
    if not os.path.exists(args.o):
        os.mkdir(args.o)

    # allocate emulators for an apk
    start_avd_serial = 5554 + args.offset * 2
    avd_serial_list = []
    for apk_index in range(args.number_of_devices):
        avd_serial = 'emulator-' + str(start_avd_serial + apk_index * 2)
        avd_serial_list.append(avd_serial)
        print('allocate emulators: %s' % avd_serial)

    if args.no_headless:
        screen_option = "\"\""
    else:
        screen_option = "-no-window"

    if args.apk is not None:
        # single apk mode
        all_apks = [args.apk]
        if args.login_script is None:
            all_apks_login_scripts = ["\"\""]
        else:
            all_apks_login_scripts = [args.login_script]
    else:
        # multiple apks mode
        all_apks, all_apks_login_scripts = get_all_apks(args.apk_list)

    if args.repeat > 1:
        copy_all_apks = all_apks.copy()
        copy_all_apks_login_scripts = all_apks_login_scripts.copy()
        for i in range(1, args.repeat):
            all_apks = all_apks + copy_all_apks
            all_apks_login_scripts = all_apks_login_scripts + copy_all_apks_login_scripts

    print("the apk list to fuzz: %s" % str(all_apks))

    number_of_apks = len(all_apks)
    apk_index = 0

    while 0 <= apk_index < number_of_apks:

        p = ThreadPool(args.number_of_devices)
        for avd_serial in avd_serial_list:
            time.sleep(10)
            if apk_index >= number_of_apks:
                break
            current_apk = all_apks[apk_index]

            print(os.path.exists(current_apk))

            print("Now allocate the apk: %s on %s" % (current_apk, avd_serial))
            login_script = all_apks_login_scripts[apk_index]
            print("its login script: %s" % login_script)

            if args.monkey:
                p.apply_async(run_monkey, args=(current_apk, avd_serial, args.avd_name,
                                                args.o, args.time, screen_option,
                                                login_script,args.snapshot,))
            elif args.ape:
                p.apply_async(run_ape, args=(current_apk, avd_serial, args.avd_name,
                                             args.o, args.time, screen_option,
                                             login_script,args.snapshot,))
            elif args.timemachine:
                avd_port = avd_serial.split('-')[1]
                p.apply_async(run_timemachine, args=(current_apk, avd_serial, args.avd_name,
                                                     args.o, args.time, screen_option,
                                                     login_script, avd_port,))
            elif args.combo:
                p.apply_async(run_combodroid, args=(current_apk, avd_serial, args.avd_name,
                                                    args.o, args.time, screen_option,
                                                    login_script,))
            elif args.combo_login:
                p.apply_async(run_combodroid_login, args=(current_apk, avd_serial, args.avd_name,
                                                          args.o, args.time, screen_option,
                                                          login_script,args.snapshot,))
            elif args.humanoid:
                p.apply_async(run_humanoid, args=(current_apk, avd_serial, args.avd_name,
                                                  args.o, args.time, screen_option,
                                                  login_script,))

            elif args.droidbot:
                p.apply_async(run_droidbot, args=(current_apk, avd_serial, args.avd_name,
                                                  args.o, args.time, screen_option,
                                                  login_script,))
            
            elif args.weighted:
                p.apply_async(run_weighted, args=(current_apk, avd_serial, args.avd_name,
                                                  args.o, args.time, screen_option,
                                                  login_script, args.snapshot,))

            elif args.stoat:
                p.apply_async(run_stoat, args=(current_apk, avd_serial, args.avd_name,
                                               args.o, args.time, screen_option,
                                               login_script,args.snapshot,))
            elif args.sapienz:
                p.apply_async(run_sapienz, args=(current_apk, avd_serial, args.avd_name,
                                                 args.o, args.time, screen_option,
                                                 login_script,args.snapshot,))

            elif args.qtesting:
                p.apply_async(run_qtesting, args=(current_apk, avd_serial, args.avd_name,
                                                  args.o, args.time, screen_option,
                                                  login_script,args.snapshot,))

            elif args.fastbot:
                p.apply_async(run_fastbot, args=(current_apk, avd_serial, args.avd_name,
                                                 args.o, args.time, screen_option,
                                                 login_script, args.snapshot,))
            elif args.newmonkey:
                p.apply_async(run_newmonkey, args=(current_apk, avd_serial, args.avd_name,
                                                   args.o, args.time, screen_option,
                                                   login_script, args.snapshot,))
            elif args.wetest:
                p.apply_async(run_wetest, args=(current_apk, avd_serial, args.avd_name,
                                                args.o, args.time, screen_option,
                                                login_script, args.snapshot,))
            elif args.fastbot_new:
                p.apply_async(run_fastbot_new, args=(current_apk, avd_serial, args.avd_name,
                                                 args.o, args.time, screen_option,
                                                 login_script, args.snapshot,))
            elif args.wetest_new:
                p.apply_async(run_wetest_new, args=(current_apk, avd_serial, args.avd_name,
                                                args.o, args.time, screen_option,
                                                login_script, args.snapshot,))
            else:
                pass

            apk_index += 1

        print("wait the allocated devices to finish...")
        p.close()
        p.join()


if __name__ == '__main__':
    ap = ArgumentParser()

    # by default, we run each bug/tool for 6h & 5r.
    # Each emulator is configured as 2GB RAM, 1GB internal storage and 1GB SDCard

    ap.add_argument('--avd', type=str, dest='avd_name', help="the device name")
    ap.add_argument('--apk', type=str, dest='apk')
    ap.add_argument('-n', type=int, dest='number_of_devices', default=1,
                    help="number of emulators created for testing, default: 1")
    ap.add_argument('--apk-list', type=str, dest='apk_list', help="list of apks under test")
    ap.add_argument('-o', required=True, help="output dir")
    ap.add_argument('--time', type=str, default='6h', help="the fuzzing time in hours (e.g., 6h), minutes (e.g., 6m),"
                                                           " or seconds (e.g., 6s), default: 6h")
    ap.add_argument('--repeat', type=int, default=1, help="the repeated number of runs, default: 1")
    ap.add_argument('--max-emu', type=int, default=16, help="the maximum allowed number of emulators")
    ap.add_argument('--no-headless', dest='no_headless', default=False, action='store_true', help="show gui")
    ap.add_argument('--login', type=str, dest='login_script', help="the script for app login")
    ap.add_argument('--snapshot', default=False, action='store_true', help="use this option if the target app is "
                                                                           "already installed in the emulator "
                                                                           "and logged in")
    ap.add_argument('--wait', type=int, dest='idle_time',
                    help="the idle time to wait before starting the fuzzing")

    # supported fuzzing tools
    ap.add_argument('--monkey', default=False, action='store_true')
    ap.add_argument('--ape', default=False, action='store_true')
    ap.add_argument('--timemachine', default=False, action='store_true')
    ap.add_argument('--combo', default=False, action='store_true')
    ap.add_argument('--combo-login', default=False, dest='combo_login', action='store_true')
    ap.add_argument('--humanoid', default=False, action='store_true')
    ap.add_argument('--droidbot', default=False, action='store_true')
    ap.add_argument('--stoat', default=False, action='store_true')
    ap.add_argument('--sapienz', default=False, action='store_true')
    ap.add_argument('--qtesting', default=False, action='store_true')
    ap.add_argument('--weighted', default=False, action='store_true')
    ap.add_argument('--fastbot', default=False, action='store_true')
    ap.add_argument('--wetest', default=False, action='store_true')
    ap.add_argument('--newmonkey', default=False, action='store_true')
    ap.add_argument('--fastbot_new', default=False, action='store_true')
    ap.add_argument('--wetest_new', default=False, action='store_true')

    ap.add_argument('--offset', type=int, default=0, help="device offset number")

    args = ap.parse_args()

    if args.number_of_devices + args.offset > 16:
        if not args.timemachine:
            # TimeMachine is allowed to run more than 16 instances due to it runs in the docker containers.
            ap.error('n + offset should not be ge 16')

    if args.apk is None and args.apk_list is None:
        ap.error('please specify an apk or an apk list')

    if args.apk_list is not None and not os.path.exists(args.apk_list):
        ap.error('No such file: %s' % args.apk_list)

    if 'h' not in args.time and 'm' not in args.time and 's' not in args.time:
        ap.error('incorrect time format, should be appended with h, m, or s')

    if args.idle_time is not None:
        for i in range(1, int(args.idle_time)):
            print("%d minutes remaining to wait ..." % (args.idle_time - i))
            time.sleep(60)

    main(args)
