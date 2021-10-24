import os.path
import re
import sys
import json
from datetime import datetime

INIT_STATE = "state_0"
FINAL_STATE = "Crash!"


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
        print("file \'%s\' doesn't exists. Analysis terminated." % file_path)
        return False
    return True


class Analyzer:

    def __init__(self, json_path: str):
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

            self.state = INIT_STATE                  # Init the state of analysis automaton
            self.states = [INIT_STATE]
            self.tf = info["transition_function"]    # Get the automaton transition function
            self.transition = []
            self.transitions: dict = dict()         # Record the happened transition chains and its occurrence time

    def is_valid_transition(self, event_id) -> bool:
        if event_id in self.tf[self.state]:
            return True
        else:
            return False

    def record_transition(self):
        if len(self.transition) > 1 and self.transition[1] != "eof":
            key = str(self.transition)
            if key in self.transitions:
                self.transitions[key] += 1
            else:
                self.transitions[key] = 1
        self.transition.clear()

    def reset_automaton(self, is_eof: bool):                  # Reset the automaton
        if is_eof:
            self.transition.append("eof")
        self.record_transition()
        self.state = INIT_STATE
        self.states.clear()

    def transit_automation(self, event_id):     # Conduct a transition of the automaton
        self.state = self.tf[self.state][event_id]
        self.states.append(self.state)
        self.transition.append(event_id)

    def analyze(self, log_path: str, time_path: str):
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

                        if self.is_valid_transition(event_id):     # If this is a valid transition then do it
                            # new_state = self.tf[self.state][event_id]
                            # if new_state in self.states and new_state != self.state:
                            #     self.record_transition()
                            #     self.states.clear()
                            self.transit_automation(event_id)
                            if self.state == FINAL_STATE:
                                self.record_transition()
                                self.reset_automaton(False)
                        else:   # If the current state doesn't have a valid transition through this event
                            self.reset_automaton(False)
                            if self.is_valid_transition(event_id):
                                self.transit_automation(event_id)

                    if re.search("Warning ", line, re.I):       # If it's a “Warning”
                        warning_id = line[re.search("Warning ", line, re.I).span()[1]]
                        self.warning_counts[warning_id] += 1

                    if re.search("Crash!", line, re.I):
                        self.is_crashed = True
                        self.crash_time.append(event_time - start_time)

            self.reset_automaton(True)
        return True

    def show_result(self, tool_name: str):
        print_title("[ %s-%s (%s) ]" % (self.app_name, self.bug_id, tool_name))
        print_header("[ The statistics of each event ]")
        zero_count = 0      # Count up the events which are never reached
        for event in self.event_counts:
            if self.event_counts[event] == 0:
                self.first_time[event] = None
                zero_count += 1
            print(" "*10 + "[ %s ] Event %s/%d: %3d-%-3d. (%s/%s)\n" %
                  (self.bug_id, event,
                   self.total_event,
                   self.event_counts[event],
                   self.warning_counts[event],
                   self.first_time[event], self.delta) +
                  " "*14 + "> event info: %s" % self.events[event]["info"])
            if self.warning_counts[event] > 0:
                print(" "*14 + "> Warning info: %s" % self.warnings[event])

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

        if len(self.transitions) != 0 and not self.is_crashed:
            count = 1
            print_header("[ Transitions happened in testing ]")
            for transition in self.transitions:
                print(" "*10 + "[Transition %d] %s" % (count, transition))
                print(" "*14 + "Count: %s" % self.transitions[transition])
                count += 1

        print_title("[ Analysis finished ]")


def main(log_dir: str):

    base_dir = os.path.basename(log_dir)
    first_pos, second_pos, third_pos, forth_pos = \
        re.search("instrumented-", base_dir).span(), \
        re.search("-#", base_dir).span(), \
        re.search(".apk.", base_dir).span(), \
        re.search(".result", base_dir).span()

    app_name, bug_id, tool_name = \
        base_dir[first_pos[1]: second_pos[0]],\
        base_dir[second_pos[0]+1: third_pos[0]],\
        base_dir[third_pos[1]: forth_pos[0]]

    json_path = os.path.join("..", app_name, "configuration-" + bug_id + ".json")       # Get the path of the json file
    analyzer = Analyzer(json_path)                                                      # Initialize an Analyzer

    log_path = os.path.join(log_dir, "logcat.log")
    print("[ Analyzer ] The log path:\n    > %s" % log_path)
    time_path = os.path.join(log_dir, tool_name + "_testing_time_on_emulator.txt")
    print("[ Analyzer ] The time record path:\n    > %s" % time_path)

    if analyzer.analyze(log_path, time_path):                                            # Start analyzing log
        analyzer.show_result(tool_name)


def help_info():
    print("[Usage]: python analyze_log.py log_path1[ log_path2[ ...]]")
    print("[Usage]: Please put log files and the json file at the same directory with the same filename.")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        help_info()
    else:
        for i in range(1, len(sys.argv)):
            main(sys.argv[i])
