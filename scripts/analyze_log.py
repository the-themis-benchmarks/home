from argparse import ArgumentParser, Namespace
import os.path
import re
import json
from datetime import datetime
import subprocess
from automata.fa.dfa import DFA
from automata.fa.nfa import NFA


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


def print_waring(w: str):
    """ Print the warning info """
    print("[ Warning ] %s" % w)


def init_counts(events: dict):
    """ Init a map to count """
    res = dict()
    for event in events:
        res[event] = 0
    return res


def file_exists(file_path: str) -> bool:
    """ Check whether the file exists """
    return os.path.exists(file_path)


def get_name(tool_name: str) -> str:
    if tool_name == "combodroid":
        return "combo"
    else:
        return tool_name


def get_time_format(tool_name: str) -> str:
    if tool_name == "combodroid":
        return "%Y-%m-%d-%H-%M-%S"
    else:
        return "%Y-%m-%d-%H:%M:%S"


def get_name(tool_name: str) -> str:
    if tool_name == "combodroid":
        return "combo"
    elif tool_name == "droidbot.dfs.greedy":
        return "droidbot"
    else:
        return tool_name


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
        if event in self.transitions[self.current_state] and self.transitions[self.current_state][event] != "{}":
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

        ''' Init the DFA graph '''
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

        ''' Floyd algorithm '''
        for i in states:
            for j in states:
                for k in states:
                    if graph[j][i] + graph[i][k] < graph[j][k]:
                        graph[j][k] = graph[j][i] + graph[i][k]

        ''' Get the shortest distance from every state in the DFA to the final state '''
        ret = dict()
        for i in states:
            graph[i][i] = 0
            ret[i] = graph[i][final_state]

        return ret


class Converter:

    def __init__(self, nfa_path: str):
        self.nfa_path = nfa_path
        self.json_path = "./converted_json.json"

    def get_converted_json(self) -> bool:
        putflap_path = "../tools/putflap.jar"
        command = "java -jar " + putflap_path + " convert -t json " + self.nfa_path
        print("[ Converter ] Executing  \"%s\"" % command)
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p.wait()
        if p.poll() == 0:
            print("[ Converter ] Conversion succeeded!")
            return True
        else:
            print("[ Converter ] Conversion failed.")
            return False

    def dfa_from_json(self) -> MyDFA:
        """ get the DFA from the .json file converted from .jff """
        with open(self.json_path, "r", encoding="utf-8") as f:
            info = json.load(f)
            raw_states = info["conversions"][0]["result"]["states"]
            raw_transitions = info["conversions"][0]["result"]["transitions"]
        print("[ Convertor ] The NFA has %d states and %d edges." % (len(raw_states), len(raw_transitions)))
        init_state = None
        final_states, states, transitions, names, input_symbols = set(), set(), dict(), dict(), set()
        for state in raw_states:
            states.add(state["name"])
            names[state["id"]] = state["name"]
            if state["type"] == "INITIAL":
                init_state = state["name"]
            if state["type"] == "FINAL":
                final_states.add(state["name"])

        for transition in raw_transitions:
            from_name = names[transition["from"]]
            to_name = names[transition["to"]]
            char = transition["read"]
            input_symbols.add(char)
            if from_name not in transitions:
                transitions[from_name] = {char: {to_name}}
            else:
                if char not in transitions[from_name]:
                    transitions[from_name][char] = {to_name}
                else:
                    transitions[from_name][char].add(to_name)

        for fn in final_states:
            if fn not in transitions:
                transitions[fn] = dict()

        # print("    < Init State > %s" % init_state)
        # print("    < Final States > %s" % str(final_states))
        # print("    < All states > %s" % str(states))
        # print("    < All Transitions > ")
        # for f in sorted(transitions.keys()):
        #     print("        %3s : %s" % (f, str(transitions[f])))

        dfa = MyDFA.from_nfa(NFA(
            states=states,
            input_symbols=input_symbols,
            transitions=transitions,
            initial_state=init_state,
            final_states=final_states
        ))

        print("[ Converter ] Loading json succeeded.")
        return dfa

    def delete_converted_json(self):
        os.remove(self.json_path)


class Analyzer:

    def __init__(self, json_path: str, args: Namespace, nfa_path: str):

        converter = None
        if nfa_path is not None:
            converter = Converter(nfa_path)

        with open(json_path, "r", encoding="utf-8") as f:
            info = json.load(f)
            self.app_name: str = info["app_name"]  # Get the name of the app
            self.bug_id: str = info["bug_id"]  # Get the bug id of
            self.events: dict = info["events"]  # Get all events
            self.warnings: dict = info["warnings"]  # Get all Warnings
            self.all_events_happened: str = info["all_events_happened"]

            self.total_event = len(self.events)  # Get the numbers of events
            self.event_counts = init_counts(self.events)  # Init event counter
            self.warning_counts = init_counts(self.events)  # Init warning counter

            self.first_time = dict()  # Record the time of first reaching event n
            self.delta = None  # This is used to record the time span of testing

            self.last_event = None
            self.last_time = None
            self.warning_pairs = init_counts(self.events)

            self.is_crashed = False  # To show whether tester reaches the crash
            self.crash_time = None  # To Record the time of crash happening

            self.fa = None
            if converter is not None:
                success = converter.get_converted_json()
                if success:
                    self.fa = converter.dfa_from_json()
                    converter.delete_converted_json()

            self.distances_record = None
            if self.fa is not None:
                self.distances_record = {self.fa.distances[self.fa.current_state]: 1}

            if "interesting_pairs" in info:
                self.ip = info["interesting_pairs"]
            else:
                self.ip = None
            if args.manual:
                self.interesting_pairs = self.load_ip_manually()
            else:
                self.interesting_pairs = self.load_ip_from_dfa()

    def load_ip_manually(self):
        if self.ip is not None:  # Get the interesting pairs
            ip: dict = dict()
            raw_ip: dict = self.ip
            for prev in raw_ip:
                for next in raw_ip[prev]:
                    if (prev + next) not in ip:
                        ip[prev + next] = 0
            if len(ip) == 0:
                print_info("No interesting pairs needed to count.")
                return None
            else:
                return ip
        else:
            print_info("No interesting pairs needed to count.")
            return None

    def load_ip_from_dfa(self):
        if self.fa is not None:
            ip: dict = dict()
            for state in self.fa.transitions.keys():
                for prev in self.fa.transitions[state].keys():
                    if prev != '' and self.fa.transitions[state][prev] != "{}":
                        to = self.fa.transitions[state][prev]
                        for next in self.fa.transitions[to].keys():
                            if next != '' and self.fa.transitions[to][next] != "{}" and (prev + next) not in ip:
                                ip[prev + next] = 0
            if len(ip) == 0:
                print_info("No interesting pairs needed to count.")
                return None
            else:
                return ip
        else:
            print_info("No interesting pairs needed to count.")
            return None

    def analyze(self, log_path: str, time_path: str, tool_name: str, args: Namespace) -> bool:
        """ Process the time file """
        if not file_exists(time_path):
            return False

        year = "2021-"
        with open(time_path, "r", encoding="utf-8") as f:
            ''' Get the time of beginning '''
            try:
                start_time = datetime.strptime(f.readline().split("\n")[0], get_time_format(tool_name))
                self.delta = start_time
                year = str(start_time.year) + "-"
            except ValueError:
                print("[ Error ] The time value is not correct in: %s" % time_path)
                return False
            ''' Get the time of finishing '''
            try:
                end_time = datetime.strptime(f.readline().split("\n")[0], get_time_format(tool_name))
            except ValueError:
                end_time = None

        """ Process the log file """
        if not file_exists(log_path):
            return False

        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:

                if not line.startswith('---'):
                    info = line.split(' ')
                    self.delta = datetime.strptime(year + info[0] + " " + info[1].split('.')[0], "%Y-%m-%d %H:%M:%S")

                if re.search("Themis", line):  # Search "Themis"

                    ''' Get the arrival time '''
                    event_time = self.delta

                    ''' Get the type of this line '''
                    match_event = re.search("Event ", line, re.I)
                    match_warning = re.search("Warning ", line, re.I)
                    line_type = ""
                    if match_event is None and match_warning is not None:
                        line_type = "Warning"
                    if match_event is not None and match_warning is None:
                        line_type = "Event"
                    if match_event is not None and match_warning is not None and match_event.span() < match_warning.span():
                        line_type = "Event"
                    if match_event is not None and match_warning is not None and match_event.span() > match_warning.span():
                        line_type = "Warning"

                    if line_type == "Event":  # If it's a "Event"

                        ''' Get event id and count it '''
                        pos = match_event.span()[1]
                        event_id = line[pos]  # To get event id
                        if event_id == ":":
                            continue
                        pos += 1
                        while line[pos] != ":":
                            event_id += line[pos]
                            pos += 1
                        event_id = event_id.strip()
                        if not ("a" <= event_id <= "z") and int(event_id) >= 10:
                            event_id = chr(int(event_id) - 10 + 97)
                        if event_id not in self.event_counts:
                            continue
                        self.event_counts[str(event_id)] += 1  # The corresponding event count add 1
                        self.last_time = event_time

                        ''' Record the relative time of first occurrence '''
                        if event_id not in self.first_time:
                            self.first_time[event_id] = event_time - start_time

                        ''' Count the interesting pairs '''
                        if self.interesting_pairs is not None and self.last_event is not None and \
                                (self.last_event + event_id) in self.interesting_pairs:
                            self.interesting_pairs[self.last_event + event_id] += 1
                        self.last_event = event_id

                        ''' Compute the transition of the converted DFA '''
                        if self.fa is not None and event_id in self.fa.input_symbols:  # if this event is not in the DFA, skip it

                            if self.fa.validate_event(event_id):  # If this is a valid transition then do it
                                self.fa.do_event(event_id)

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

                    if line_type == "Warning":  # If it's a “Warning”
                        pos = match_warning.span()[1]
                        warning_id = line[pos]  # To get event id
                        if warning_id == ":":
                            continue
                        pos += 1
                        while line[pos] != ":":
                            warning_id += line[pos]
                            pos += 1
                        warning_id = warning_id.strip()
                        if not ("a" <= warning_id <= "z") and int(warning_id) >= 10:
                            warning_id = chr(int(warning_id) - 10 + 97)
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

            if self.fa is not None:
                self.fa.reset_current_state()

        ''' If no finish time in time files, use the last line log time to compute the time interval '''
        if end_time is None:
            self.delta = self.delta - start_time
        else:
            self.delta = end_time - start_time
        return True

    def show_result(self, tool_name: str) -> dict:
        print_title("[ %s-%s (%s) ]" % (self.app_name, self.bug_id, tool_name))

        ''' Basic module '''
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
                print(" " * 14 + "> Event info: %s" % self.events[event]["info"])
                if self.warning_counts[event] > 0:
                    if event in self.warning_pairs:
                        print(" " * 14 + "> Warning info: %s [immediately occurrence (<1s): %d]"
                              % (self.warnings[event], self.warning_pairs[event]))
                    else:
                        print(" " * 14 + "> Warning info: %s"
                              % self.warnings[event])

        ''' Detail module '''
        if args.detail and zero_count != 0:  # If there is any event that its `count` > 0
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

        if args.detail and self.interesting_pairs is not None:
            print_header(" [ The count of interesting pairs ] ")
            for pair in sorted(self.interesting_pairs.keys()):
                print(" " * 10 + "[ %s ] (%s, %s) : %4d times" % (
                    self.bug_id, pair[0], pair[1], self.interesting_pairs[pair]))

        ''' DFA '''
        if args.detail and self.fa is not None and len(self.distances_record) != 0:
            print_header("[ The minimum distance to the crash when testing ]")
            distances = sorted(self.distances_record.keys())
            for distance in distances:
                print(" " * 10 + "[ %s ] Min distance %s/%s (%d times)"
                      % (self.bug_id,
                         distance, self.fa.distances[self.fa.initial_state],
                         self.distances_record[distance]))

        result = dict()
        result["metrics"] = self.show_metrics()

        print_title("[ Analysis finished ]")

        return result

    def prepare_metrics(self) -> dict:
        """ Prepare the metrics of estimation results """

        metrics = dict()

        if self.events is None or len(self.events) == 0:
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

        if self.interesting_pairs is None or len(self.interesting_pairs) == 0:
            metrics["covered_pairs"] = "None"
            metrics["all_pairs"] = "None"
            metrics["pairs_coverage"] = "None"
        else:
            metrics["covered_pairs"] = 0
            metrics["all_pairs"] = str(len(self.interesting_pairs.keys()))
            for pair in self.interesting_pairs.keys():
                if self.interesting_pairs[pair] != 0:
                    metrics["covered_pairs"] += 1
            metrics["pairs_coverage"] = ("%3.2f" % (
                        metrics["covered_pairs"] * 100 / len(self.interesting_pairs.keys()))) + "%"
            metrics["covered_pairs"] = str(metrics["covered_pairs"])

        if self.distances_record is None:
            metrics["min_distance"] = "None"
        else:
            metrics["min_distance"] = str(min(sorted(self.distances_record.keys())))

        return metrics

    def show_metrics(self, ) -> str:
        print_header("[ COVERAGE METRICS ]")
        metrics = self.prepare_metrics()
        print(" " * 10 + "          Event Coverage(%)     Event-Pair Coverage(%)    Min Distance")
        print(" " * 10 + "[ %s ]   %2s/%-2s(%s)            %2s/%-2s(%s)              %2s"
              % (self.bug_id,
                 metrics["covered_events"], metrics["all_events"], metrics["events_coverage"],
                 metrics["covered_pairs"], metrics["all_pairs"], metrics["pairs_coverage"],
                 metrics["min_distance"]))
        return "%s / %s / %s / %s" % (
        metrics["events_coverage"], metrics["pairs_coverage"], metrics["min_distance"], self.is_crashed)


def main(args: Namespace) -> dict:
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

    ''' Load the configuration file '''
    json_path = os.path.join("..", app_name, "configuration-" + bug_id + ".json")  # Get the path of the json file
    if not file_exists(json_path):
        print_error("%s does not exists! Analysis aborted." % json_path)
        return dict()

    ''' Load the NFA file '''
    nfa_path = os.path.join("..", app_name, bug_id[1:] + "-NFA.jff")
    if not file_exists(nfa_path):
        print_waring("No NFA the use. Analyzer will only count events.")
        nfa_path = None
    else:
        print_info("THE NFA FILE:\n    > %s" % nfa_path)

    ''' Initialize an Analyzer '''
    analyzer = Analyzer(json_path, args, nfa_path)

    ''' Load the log file '''
    log_path = os.path.join(log_dir, "logcat.log")
    if not file_exists(log_path):
        print_error("%s does not exists! Analysis aborted." % log_path)
        return dict()
    print_info("THE LOG FILE:\n    > %s" % log_path)

    ''' Load the time file '''

    time_path = os.path.join(log_dir, get_name(tool_name) + "_testing_time_on_emulator.txt")
    if not file_exists(time_path):
        print_error("%s does not exists! Analysis aborted." % time_path)
        return dict()
    print_info("THE TIME FILE:\n    > %s" % time_path)

    ''' Start analyzing log '''
    result = dict()
    if analyzer.analyze(log_path, time_path, tool_name, args):
        result: dict = analyzer.show_result(tool_name)
        result["app_name"] = app_name
        result["bug_id"] = bug_id
        result["tool_name"] = tool_name

    return result


if __name__ == "__main__":

    parser = ArgumentParser(prog="Log Analyzer", usage="to analyze the output logs of running testers.")

    parser.add_argument("-w", "--wait", action="store_true", default=False,
                        help="let the FA wait at the current state when mismatching")
    parser.add_argument("-m", "--manual", action="store_true", default=False,
                        help="Manually specify the interesting pairs")
    parser.add_argument("-d", "--detail", action="store_true", default=False, help="Show more details")
    parser.add_argument("-a", "--all", action="store_true", default=False,
                        help="Parse the argument `target_dir` as the parent dir of result dirs")

    parser.add_argument("target_dir", help="the output logs dir that to be analyzed")

    args = parser.parse_args()
    print_info("ARGUMENTS:\n"
               + "    > Target directory: [%s]\n" % args.target_dir
               + "    > Do count all pairs in DFA? [%s]\n" % args.manual
               + "    > Do wait when matching? [%s]" % args.wait
               + "    > Use the parent dir? [%s]" % args.all)

    if args.all:
        parent_dir = args.target_dir
        results = dict()
        with os.scandir(parent_dir) as dirs:

            sorted_dirs = []
            for sud_dir in dirs:
                sorted_dirs.append(sud_dir.name)

            for sub_dir in sorted(sorted_dirs):

                if sub_dir.find("instrumented-") == -1:
                    continue

                args.target_dir = os.path.join(parent_dir, sub_dir)
                result = main(args)
                if len(result) == 0:  # No valid result
                    continue

                app_name, bug_id, tool_name = result["app_name"], result["bug_id"], result["tool_name"]

                if tool_name not in results:
                    results[tool_name] = dict()
                if app_name not in results[tool_name]:
                    results[tool_name][app_name] = dict()
                if bug_id not in results[tool_name][app_name]:
                    results[tool_name][app_name][bug_id] = []

                results[tool_name][app_name][bug_id].append(result["metrics"])

        tools = sorted(results.keys())
        for tool in tools:
            print("[%s]" % tool)
            apps = sorted(results[tool].keys())
            for app in apps:
                print("    [%s]" % app)
                bugs = results[tool][app].keys()
                for bug in bugs:
                    metrics = results[tool][app][bug]
                    print("        [%s] %s" % (bug, str(metrics)))
                    max_EC, max_EPC, min_MD = 0, 0, 1000
                    for metric in metrics:
                        metric_record = metric.split('/')

                        EC = None
                        if metric_record[0].strip() == "None":
                            max_EC = None
                        else:
                            EC = float(metric_record[0][:-2].strip())

                        EPC = None
                        if metric_record[1].strip() == "None":
                            max_EPC = None
                        else:
                            EPC = float(metric_record[1][:-2].strip())
                        MD = None
                        if metric_record[2].strip() == "None":
                            min_MD = None
                        else:
                            MD = int(metric_record[2].strip())

                        if EC is not None and EC > max_EC:
                            max_EC = EC
                        if EPC is not None and EPC > max_EPC:
                            max_EPC = EPC
                        if MD is not None and MD < min_MD:
                            min_MD = MD

                    print("        [%s-best] %s" % (bug, str(max_EC) + " & " + str(max_EPC) + " & " + str(min_MD)))

    else:
        main(args)
