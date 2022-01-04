from argparse import ArgumentParser, Namespace
import os.path
import re
import json
from datetime import datetime
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA

INIT_STATE = "state_0"
FINAL_STATE = "Crash!"


def print_header(header: str):
    """ Print the header of each section """
    com_len = int((100 - len(header)) / 2)
    print("-" * com_len + header + "-" * com_len)


def print_title(title: str):
    """ Print the title """
    com_len = int((100 - len(title)) / 2)
    print("*" * com_len + title + "*" * com_len)


def print_info(info: str):
    """ Print the info with tag \'Analyzer\' """
    print("[ Analyzer ] %s" % info)


def print_error(e: str):
    """ Print the info which means that a error happens """
    print("[  Error  ] %s" % e)


def init_counts(events: dict):
    """ Init a map to count """
    res = dict()
    for event in events:
        res[event] = 0
    return res


def file_exists(file_path: str):
    """ Check whether the file exists """
    if not os.path.exists(file_path):
        print_error("file \'%s\' doesn't exists. Analysis terminated." % file_path)
        return False
    return True


class MyDFA(DFA):

    def __init__(self, *, states, input_symbols, transitions,
                 initial_state, final_states, allow_partial=False):
        DFA.__init__(self, states=states, input_symbols=input_symbols, transitions=transitions,
                     initial_state=initial_state, final_states=final_states, allow_partial=allow_partial)
        self.current_state = initial_state
        self.distances = self._shortest_distances()

    def reset_current_state(self):
        self.current_state = self.initial_state

    def validate_event(self, event) -> bool:
        """ To validate an event """
        if event in self.transitions[self.current_state]:
            return True
        else:
            return False

    def do_event(self, event):
        """ Change the state of the DFA according to the transitions """
        self.current_state = self._get_next_current_state(self.current_state, event)

    def now_distance(self):
        return self.distances[self.current_state]

    def _shortest_distances(self) -> dict:
        """ Compute the shortest distance from every state to the final state """
        states = self.states
        if '{}' in states:
            states.remove('{}')
        final_state = self.final_states.copy().pop()

        """ Init the DFA graph """
        graph = dict()
        for state_from in states:
            if state_from == '{}':
                continue
            graph[state_from] = dict()
            for state_to in states:
                if state_to == '{}':
                    continue
                if state_to in self.transitions[state_from].values():
                    graph[state_from][state_to] = 1
                else:
                    graph[state_from][state_to] = 1000

        """ Floyd algorithm """
        for i in states:
            for j in states:
                for k in states:
                    if graph[j][i] + graph[i][k] < graph[j][k]:
                        graph[j][k] = graph[j][i] + graph[i][k]

        """ Get the shortest distance from every state in the DFA to the final state """
        ret = dict()
        for i in states:
            graph[i][i] = 0
            ret[i] = graph[i][final_state]

        return ret


class Analyzer:

    def __init__(self, json_path: str, args: Namespace):

        with open(json_path, "r", encoding="utf-8") as f:
            info = json.load(f)
            self.app_name: str = info["app_name"]  # Get the name of the app
            self.bug_id: str = info["bug_id"]  # Get the bug id of
            self.events: dict = info["events"]  # Get all events
            self.warnings: dict = info["warnings"]  # Get all Warnings
            self.all_events_happened: str = info["all_events_happened"]
            self.has_fa = len(info["transition_function"]) != 0

            if "interesting_pairs" in info:  # Get the intesesting pairs
                self.interesting_pairs: dict = dict()
                ip: dict = info["interesting_pairs"]
                for prev in ip:
                    for next in ip[prev]:
                        self.interesting_pairs[prev + next] = 0
            else:
                print_info("No interesting pairs needed to count.")
                self.interesting_pairs = None

            self.total_event = len(self.events)  # Get the numbers of events
            self.event_counts = init_counts(self.events)  # Init event counter
            self.warning_counts = init_counts(self.events)  # Init warning counter

            self.first_time = dict()  # Record the time of first reaching event n
            self.delta = None  # This is used to record the time span of testing

            self.last_event = None
            self.last_time = None
            self.warning_pairs = init_counts(self.events)

            self.distances_record = dict()

            self.is_crashed = False  # To show whether tester reaches the crash
            self.crash_time = None  # To Record the time of crash happening

            if self.has_fa:
                states = set(info["transition_function"].keys())
                states.add(FINAL_STATE)
                if args.dfa:  # use DFA
                    transitions = info["transition_function"]
                    transitions[FINAL_STATE] = dict()
                    self.fa = MyDFA(
                        states=states,
                        input_symbols=set(self.events.keys()),
                        transitions=transitions,
                        initial_state=INIT_STATE,
                        final_states={FINAL_STATE},
                        allow_partial=True
                    )
                if args.nfa:  # use NFA
                    self.fa = MyDFA.from_nfa(NFA(
                        states=states,
                        input_symbols=set(self.events.keys()),
                        transitions=info["transition_function"],
                        initial_state=INIT_STATE,
                        final_states={FINAL_STATE},
                    ))

    def analyze(self, log_path: str, time_path: str, args: Namespace):
        """ Process the time file """
        if not file_exists(time_path):
            return False
        with open(time_path, "r", encoding="utf-8") as f:
            ''' Get the time of beginning '''
            try:
                start_time = datetime.strptime(f.readline().split("\n")[0], "%Y-%m-%d-%H:%M:%S")
            except ValueError:
                print("[ Error ] The time value is not correct in: %s" % time_path)
                return False
            ''' Get the time of finishing '''
            try:
                end_time = datetime.strptime(f.readline().split("\n")[0], "%Y-%m-%d-%H:%M:%S")
            except ValueError:
                end_time = None

        """ Process the log file """
        if not file_exists(log_path):
            return False
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:

                if not line.startswith('---'):
                    info = line.split(' ')
                    self.delta = datetime.strptime("2021-" + info[0] + " " + info[1].split('.')[0], "%Y-%m-%d %H:%M:%S")

                if re.search("Themis", line):  # Search "Themis"

                    """ Get the arrival time """
                    event_time = self.delta

                    if re.search("Event ", line, re.I):  # If it's a "Event"

                        event_id = line[re.search("event ", line, re.I).span()[1]]  # To get event id
                        if event_id not in self.event_counts:
                            continue
                        if int(event_id) >= 10:
                            event_id = chr(int(event_id) - 10 + 97)
                        self.event_counts[str(event_id)] += 1  # The corresponding event count add 1
                        self.last_time = event_time

                        if event_id not in self.first_time:  # Record the relative time of first occurrence
                            self.first_time[event_id] = event_time - start_time

                        if self.has_fa and args.dfa:  # When input configuration file is a DFA
                            if self.fa.validate_event(event_id):  # If this is a valid transition then do it
                                old_state = self.fa.current_state
                                self.fa.do_event(event_id)

                                if old_state != self.fa.current_state:  # Count the ip
                                    if self.interesting_pairs is not None and self.last_event is not None and (
                                            self.last_event + event_id) in self.interesting_pairs:
                                        self.interesting_pairs[self.last_event + event_id] += 1
                                    self.last_event = event_id  # If there is a transition then update the last event

                                distance = self.fa.now_distance()
                                if distance in self.distances_record:
                                    self.distances_record[distance] += 1
                                else:
                                    self.distances_record[distance] = 1
                                if self.fa.current_state in self.fa.final_states:
                                    self.fa.reset_current_state()
                            else:  # If the current state doesn't have a valid transition through this event
                                if not args.wait:
                                    self.fa.reset_current_state()
                                    if self.fa.validate_event(event_id):
                                        self.fa.do_event(event_id)

                        if self.has_fa and args.nfa:  # When input configuration file is a NFA
                            # TODO: Complete the procedure when dealing a NFA-input
                            pass

                    if re.search("Warning ", line, re.I):  # If it's a “Warning”
                        warning_id = line[re.search("Warning ", line, re.I).span()[1]]
                        if warning_id not in self.warning_counts:
                            continue
                        self.warning_counts[warning_id] += 1
                        if self.last_event == warning_id and event_time.timestamp() - self.last_time.timestamp() <= 1.0:
                            if warning_id in self.warning_pairs:
                                self.warning_pairs[warning_id] = 1
                            else:
                                self.warning_pairs[warning_id] += 1

                    if re.search("Crash!", line, re.I):
                        self.is_crashed = True
                        if self.crash_time is None:
                            self.crash_time = event_time - start_time

            if self.has_fa and args.dfa:
                self.fa.reset_current_state()

            if self.has_fa and args.nfa:
                # TODO: Complete the procedure when dealing a NFA-input
                pass

        """ If no finish time in time files, use the last line log time to compute the time interval """
        if end_time is None:
            self.delta = self.delta - start_time
        else:
            self.delta = end_time - start_time
        return True

    def show_result(self, tool_name: str):
        print_title("[ %s-%s (%s) ]" % (self.app_name, self.bug_id, tool_name))

        """ Basic module """
        zero_count = 0  # Count up the events which are never reached
        if len(self.events) != 0:
            print_header("[ The statistics of each event ]")
            for event in self.event_counts:
                if self.event_counts[event] == 0:
                    self.first_time[event] = None
                    zero_count += 1
                print(" " * 10 + "[ %s ] Event %s/%d: %3d-%-3d. (%s/%s)" %
                         (self.bug_id, event,
                          self.total_event,
                          self.event_counts[event],
                          self.warning_counts[event],
                          self.first_time[event], self.delta))
                print(" " * 14 + "> Event info: %s"
                         % self.events[event]["info"])
                if self.warning_counts[event] > 0:
                    if event in self.warning_pairs:
                        print(" " * 14 + "> Warning info: %s [immediately occurrence (<1s): %d]"
                                 % (self.warnings[event], self.warning_pairs[event]))
                    else:
                        print(" " * 14 + "> Warning info: %s"
                                 % self.warnings[event])

        if zero_count != 0:  # If there is any event that its `count` > 0
            print_header("[ Analysis of the missing events ]")
            for event in self.event_counts:
                if self.event_counts[event] == 0:
                    print(" " * 10 + "[ %s ] Event %s" % (self.bug_id, event))
                    print(" " * 14 + "> The possible reason: %s" % self.events[event]["reason"])
                    print(" " * 14 + "> The previous related events: %s" % self.events[event]["dependency"])

        if zero_count == 0 and not self.is_crashed:  # If there is not any event that its `count` > 0
            print_header("[ All events reached but crash doesn't occur ]")
            print(" " * 10 + "[ %s ] The possible reason for this: %s" % (self.bug_id, self.all_events_happened))

        if self.is_crashed:
            print_header("[ The first time of crash ]")
            print(" " * 10 + "[ %s ] The min time taken to reach the crash: %s" % (self.bug_id, str(self.crash_time)))

        if self.interesting_pairs is not None:
            print_header(" [ The count of interesting pairs ] ")
            for pair in self.interesting_pairs:
                print(" " * 10 + "[ %s ] (%s, %s) : %4d times" % (
                    self.bug_id, pair[0], pair[1], self.interesting_pairs[pair]))

        ''' DFA '''
        if self.has_fa and args.dfa and len(self.distances_record) != 0:
            print_header("[ The minimum distance to the crash when testing ]")
            distances = sorted(self.distances_record.keys())
            for distance in distances:
                print(" " * 10 + "[ %s ] Min distance %s/%s (%d times)"
                        % (self.bug_id,
                           distance, self.fa.distances[self.fa.initial_state],
                           self.distances_record[distance]))

        self.show_metrics()

        print_title("[ Analysis finished ]")

    def prepare_metrics(self) -> dict:
        """ Prepare the metrics of estimation results """

        metrics = dict()

        if self.events is None:
            metrics["covered_events"] = "None"
            metrics["all_events"] = "None"
            metrics["events_coverage"] = "None"
        else:
            metrics["covered_events"] = 0
            metrics["all_events"] = str(len(self.events.keys()))
            for event in self.events:
                if self.event_counts[event] != 0:
                    metrics["covered_events"] += 1
            metrics["events_coverage"] = ("%.2f" % (metrics["covered_events"] * 100 / len(self.events.keys()))) + "%"
            metrics["covered_events"] = str(metrics["covered_events"])

        if self.interesting_pairs is None:
            metrics["covered_pairs"] = "None"
            metrics["all_pairs"] = "None"
            metrics["pairs_coverage"] = "None"
        else:
            metrics["covered_pairs"] = 0
            metrics["all_pairs"] = str(len(self.interesting_pairs.keys()))
            for pair in self.interesting_pairs.keys():
                if self.interesting_pairs[pair] != 0:
                    metrics["covered_pairs"] += 1
            metrics["pairs_coverage"] = ("%3.2f" % (metrics["covered_pairs"] * 100 / len(self.interesting_pairs.keys()))) + "%"
            metrics["covered_pairs"] = str(metrics["covered_pairs"])

        if len(self.distances_record) == 0:
            metrics["min_distance"] = "None"
        else:
            metrics["min_distance"] = str(min(sorted(self.distances_record.keys())))

        return metrics

    def show_metrics(self):
        print_header("[ COVERAGE METRICS ]")
        metrics = self.prepare_metrics()
        print(" "*10 + "           Event Coverage(%)     Event-Pair Coverage(%)    Min Distance")
        print(" "*10 + "[ %s ]   %2s/%-2s(%s)            %2s/%-2s(%s)              %2s"
              % (self.bug_id,
                 metrics["covered_events"], metrics["all_events"], metrics["events_coverage"],
                 metrics["covered_pairs"], metrics["all_pairs"], metrics["pairs_coverage"],
                 metrics["min_distance"]))


def main(args: Namespace):
    log_dir: str = args.target_dir

    if log_dir.endswith("/"):
        log_dir = log_dir[:len(log_dir) - 1]

    base_dir = os.path.basename(log_dir)
    first_pos, second_pos, third_pos, forth_pos = \
        re.search("instrumented-", base_dir).span(), \
        re.search("-#", base_dir).span(), \
        re.search(".apk.", base_dir).span(), \
        re.search(".result", base_dir).span()

    app_name, bug_id, tool_name = \
        base_dir[first_pos[1]: second_pos[0]], \
        base_dir[second_pos[0] + 1: third_pos[0]], \
        (base_dir[third_pos[1]: forth_pos[0]]).lower()

    json_path = os.path.join("..", app_name, "configuration-" + bug_id + ".json")  # Get the path of the json file
    analyzer = Analyzer(json_path, args)  # Initialize an Analyzer

    log_path = os.path.join(log_dir, "logcat.log")
    print_info("THE LOG FILE:\n    > %s" % log_path)
    time_path = os.path.join(log_dir, tool_name + "_testing_time_on_emulator.txt")
    print_info("THE TIME FILE:\n    > %s" % time_path)

    if analyzer.analyze(log_path, time_path, args):  # Start analyzing log
        analyzer.show_result(tool_name)


if __name__ == "__main__":
    parser = ArgumentParser(prog="Log Analyzer", usage="to analyze the output logs of running testers.")

    parser.add_argument("-d", "--dfa", action="store_true", default=False, help="use dfa style configuration file")
    parser.add_argument("-n", "--nfa", action="store_true", default=False, help="use nfa style configuration file")
    parser.add_argument("-w", "--wait", action="store_true", default=False,
                       help="let the fa wait at the current state when mismatching")

    parser.add_argument("target_dir", help="the output logs dir that to be analyzed")

    args = parser.parse_args()
    print_info("ARGUMENTS:\n    > Use DFA? [%s]\n" % args.dfa
              + "    > Use NFA? [%s]\n" % args.nfa
              + "    > Target directory: [%s]\n" % args.target_dir
              + "    > Do wait when matching? [%s]" % args.wait)

    main(args)
