from argparse import ArgumentParser, Namespace
import subprocess
import os.path
import re
import json
from datetime import datetime

INIT_STATE = "state_0"
FINAL_STATE = "Crash!"
DERIVE_PATH = "../tools/regex"


def print_header(header: str):
    com_len = int((80 - len(header)) / 2)
    print("-" * com_len + header + "-" * com_len)


def print_title(title: str):
    com_len = int((80 - len(title)) / 2)
    print("*" * com_len + title + "*" * com_len)


def init_counts(events: dict):
    res = dict()
    for event in events:
        res[event] = 0
    return res


def file_exists(file_path: str):
    if not os.path.exists(file_path):
        print("[ Warning ] file \'%s\' doesn't exists. Analysis terminated." % file_path)
        return False
    return True


def call_regex(command: str) -> str:
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    if p.poll() == 0:
        return p.communicate()[0].decode('utf-8').strip()
    else:
        print("[ warning ] Call RegEx failed!")
        return ""


class DFA:

    def __init__(self, init_state: str, final_state: str, transition_function: dict):
        self.state = init_state             # Init the state of analysis automaton
        self.init_state = init_state
        self.final_state = final_state

        self.max_event_id = 0
        self.tf = transition_function       # Get the automaton transition function
        self.transition = []                # Record the current transition path
        self.transitions: dict = dict()     # Record the happened transition chains and its occurrence time

    def is_valid_transition(self, event_id: str) -> bool:
        return event_id in self.tf[self.state]

    def transit(self, event_id):     # Conduct a transition of the automaton
        self.state = self.tf[self.state][event_id]
        self.transition.append(event_id)

    def record_transition(self):
        if len(self.transition) > 1 and self.transition[1] != "eof":
            key = str(self.transition)
            if key in self.transitions:
                self.transitions[key] += 1
            else:
                self.transitions[key] = 1

    def reset(self, is_eof: bool):
        if is_eof:
            self.transition.append("eof")
        self.record_transition()
        self.state = INIT_STATE
        self.transition.clear()


class Deriver:

    def __init__(self, derive_path: str, regex: str):
        self.path = derive_path
        self.original_regex = regex
        self.derived_regex = regex
        self.derivatives = dict()
        self.distance_left = dict()     # To record the distance left when the result of derived regex
                                        # is empty string of empty set

    def derive(self, s: str) -> str:
        command = self.path + " -e \"" + self.derived_regex + "\" -x \"" + s + "\" -n 1"
        derived_regex = call_regex(command)
        return derived_regex

    def min_len(self) -> int:
        command = self.path + " -e \"" + self.derived_regex + "\" -l"
        return int(call_regex(command))

    def record_distance(self, distance: int):
        if distance in self.distance_left:
            self.distance_left[distance] += 1
        else:
            self.distance_left[distance] = 1

    def reset(self):
        if self.derived_regex != self.original_regex:
            self.record_distance(self.min_len())
            self.derived_regex = self.original_regex

    def record_regex(self):
        if self.derived_regex in self.derivatives:
            self.derivatives[self.derived_regex] += 1
        else:
            self.derivatives[self.derived_regex] = 1


class Analyzer:

    def __init__(self, json_path: str, args: Namespace):
        with open(json_path, "r", encoding="utf-8") as f:
            info = json.load(f)
            self.app_name = info["app_name"]                            # Get the name of the app
            self.bug_id = info["bug_id"]                                # Get the bug id of
            self.events = info["events"]                                # Get all events
            self.total_event = len(self.events)                         # Get the numbers of events
            self.event_counts = init_counts(self.events)                # Init event counter
            self.warning_counts = init_counts(self.events)              # Init warning counter
            self.warnings = info["warnings"]                            # Get all Warnings
            self.all_events_happened = info["all_events_happened"]
            self.first_time = dict()                # Record the time of first reaching event n
            self.delta = None                       # This is used to record the time span of testing

            self.is_crashed = False                 # To show whether tester reaches the crash
            self.crash_time = []                    # To Record the time of crash happening

            if args.dfa:    # enable DFA
                self.dfa = DFA(INIT_STATE, FINAL_STATE, info["transition_function"])

            if args.derivative:     # enable to derive the regex
                self.deriver = Deriver(DERIVE_PATH, info["regex"])

    def analyze(self, log_path: str, time_path: str, args: Namespace):
        # Process the time file
        if not file_exists(time_path):
            return False
        with open(time_path, "r", encoding="utf-8") as f:
            start_time = datetime.strptime(f.readline().split("\n")[0], "%Y-%m-%d-%H:%M:%S")
            self.delta = datetime.strptime(f.readline().split("\n")[0], "%Y-%m-%d-%H:%M:%S") - start_time

        # Process the log file
        if not file_exists(log_path):
            return False
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:
                if re.search("Themis", line):       # Search “Themis"

                    # Get the arrival time
                    info = line.split(' ')
                    event_time = datetime.strptime("2021-" + info[0] + " " + info[1].split('.')[0], "%Y-%m-%d %H:%M:%S")

                    if re.search("Event ", line, re.I):          # If it's a "Event"

                        event_id = line[re.search("event ", line, re.I).span()[1]]    # To get event id
                        self.event_counts[str(event_id)] += 1                   # The corresponding event count add 1

                        if event_id not in self.first_time:     # Record the relative time of first occurrence
                            self.first_time[event_id] = event_time - start_time

                        if args.dfa:
                            if self.dfa.is_valid_transition(event_id):     # If this is a valid transition then do it
                                self.dfa.max_event_id = max(int(self.dfa.max_event_id), int(event_id))
                                self.dfa.transit(event_id)
                                if self.dfa.state == self.dfa.final_state:
                                    self.dfa.reset(False)
                            else:   # If the current state doesn't have a valid transition through this event
                                self.dfa.reset(False)
                                if self.dfa.is_valid_transition(event_id):
                                    self.dfa.transit(event_id)

                        if args.derivative:
                            derived_regex = self.deriver.derive(event_id)
                            if derived_regex == "P":                # If the s^(-1)R is empty set
                                self.deriver.reset()
                                derived_regex = self.deriver.derive(event_id)
                                if derived_regex != "P":
                                    self.deriver.derived_regex = derived_regex
                            else:
                                self.deriver.derived_regex = derived_regex
                                if self.deriver.derived_regex == "E":
                                    # If the s^(-1)R is empty string
                                    self.deriver.reset()
                                else:                               # If the s^(-1)R is valid
                                    self.deriver.record_distance(self.deriver.min_len())

                    if re.search("Warning ", line, re.I):       # If it's a “Warning”
                        warning_id = line[re.search("Warning ", line, re.I).span()[1]]
                        self.warning_counts[warning_id] += 1

                    if re.search("Crash!", line, re.I):
                        self.is_crashed = True
                        self.crash_time.append(event_time - start_time)

            if args.dfa:
                self.dfa.reset(True)

            if args.derivative:
                self.deriver.reset()
        return True

    def show_result(self, tool_name: str):
        print_title("[ %s-%s (%s) ]" % (self.app_name, self.bug_id, tool_name))

        # Basic module
        print_header("[ The statistics of each event ]")
        zero_count = 0      # Count up the events which are never reached
        for event in self.event_counts:
            if self.event_counts[event] == 0:
                self.first_time[event] = None
                zero_count += 1
            print(" "*10 + "[ %s ] Event %s/%d: %3d-%-3d. (%s/%s)" %
                  (self.bug_id, event,
                   self.total_event,
                   self.event_counts[event],
                   self.warning_counts[event],
                   self.first_time[event], self.delta))
            print(" " * 14 + "> Event info: %s" % self.events[event]["info"])
            if self.warning_counts[event] > 0:
                print(" "*14 + "> Warning info: %s" % self.warnings[event])

            distance_left = len(self.event_counts) - int(event)
            if args.derivative:
                if distance_left in self.deriver.distance_left:
                    print(" " * 14 + "> 1~%s occurred %s times." % (event, self.deriver.distance_left[distance_left]))
                else:
                    print(" " * 14 + "> 1~%s occurred %s times." % (event, 0))

        if zero_count != 0:     # If there is any event that its `count` > 0
            print_header("[ Analysis of the missing events ]")
            for event in self.event_counts:
                if self.event_counts[event] == 0:
                    print(" "*10 + "[ %s ] Event %s" % (self.bug_id, event))
                    print(" "*14 + "> The possible reason: %s" % self.events[event]["reason"])
                    print(" "*14 + "> The previous related events: %s" % self.events[event]["dependency"])

        if zero_count == 0 and not self.is_crashed:     # If there is not any event that its `count` > 0
            print_header("[ All events reached but crash doesn't occur ]")
            print(" "*10 + "[ %s ] The possible reason for this: %s" % (self.bug_id, self.all_events_happened))

        if self.is_crashed:
            print_header("[ The crash counts and times ]")
            print(" "*10 + "[ %s ] Crash occurred %d times." % (self.bug_id, len(self.crash_time)))
            print(" "*14 + "> The min time taken to reach the crash: %s" % str(self.crash_time[0]))
        else:
            # DFA
            if args.dfa:
                print_header("[ The deepest event tester have reached is %d ]" % self.dfa.max_event_id)

                if args.show_all and len(self.dfa.transitions) != 0:
                    count = 1
                    print_header("[ Transitions happened ]")
                    for transition in self.dfa.transitions:
                        print(" "*10 + "[Transition %d] %s" % (count, transition))
                        print(" "*14 + "Count: %s" % self.dfa.transitions[transition])
                        count += 1

            # Derivative
            # if args.derivative:
                # print_header("[ The minimum distance to the crash is %d ]" % self.deriver.min_distance)
                #
                # if args.show_all and len(self.deriver.derivatives) != 0:
                #     count = 1
                #     print_header("[ Derived regexes ]")
                #     for derived_regex in self.deriver.derivatives:
                #         print(" "*10 + "[Regex %d] %s" % (count, derived_regex))
                #         print(" "*14 + "Count: %d" % self.deriver.derivatives[derived_regex])
                #         count += 1

        print_title("[ Analysis finished ]")


def main(args: Namespace):

    log_dir: str = args.target_dir

    if log_dir.endswith("/"):
        log_dir = log_dir[:len(log_dir)-1]

    base_dir = os.path.basename(log_dir)
    first_pos, second_pos, third_pos, forth_pos = \
        re.search("instrumented-", base_dir).span(), \
        re.search("-#", base_dir).span(), \
        re.search(".apk.", base_dir).span(), \
        re.search(".result", base_dir).span()

    app_name, bug_id, tool_name = \
        base_dir[first_pos[1]: second_pos[0]],\
        base_dir[second_pos[0]+1: third_pos[0]],\
        (base_dir[third_pos[1]: forth_pos[0]]).lower()

    json_path = os.path.join("..", app_name, "configuration-" + bug_id + ".json")       # Get the path of the json file
    analyzer = Analyzer(json_path, args)                                                      # Initialize an Analyzer

    log_path = os.path.join(log_dir, "logcat.log")
    print("[ Analyzer ] The log path:\n    > %s" % log_path)
    time_path = os.path.join(log_dir, tool_name + "_testing_time_on_emulator.txt")
    print("[ Analyzer ] The time record path:\n    > %s" % time_path)

    if analyzer.analyze(log_path, time_path, args):                                            # Start analyzing log
        analyzer.show_result(tool_name)


if __name__ == "__main__":

    parser = ArgumentParser(prog="Log Analyzer", usage="to analyze the output logs of running testers.")

    parser.add_argument("-d", "--dfa", action="store_true", default=False, help="use dfa")
    parser.add_argument("-D", "--derivative", action="store_true", default=False, help="use the derivative of regex")
    parser.add_argument("-s", "--show_all", action="store_true", default=False, help="show all the valid paths")

    parser.add_argument("target_dir", help="the output logs dir that to be analyzed")

    args = parser.parse_args()
    print(args)

    main(args)
