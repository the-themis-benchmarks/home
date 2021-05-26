import csv
import os
from argparse import ArgumentParser
from typing import Dict, List

common_bugs_data = {

    "monkey_ape":  {
        'AnkiDroid': ['4707', '4451', '5756', '4977'],
        'geohashdroid': ['73'],
        'openlauncher': ['67'],
        'APhotoManager': ['116'],
        'AmazeFileManager': ['1837'],
        'FirefoxLite': ['4881'],
        'collect': ['3222'],
        'WordPress': ['11135', '10302'],
        'nextcloud': ['5173', '4026', '1918'],
        'commons': ['2123'],
        'Omni-Notes': ['745']
    },

    "monkey_combo" : {
        'AnkiDroid': ['5756', '4977'],
        'geohashdroid': ['73'],
        'openlauncher': ['67'],
        'APhotoManager': ['116'],
        'FirefoxLite': ['4881'],
        'WordPress': ['11135', '10302'],
        'nextcloud': ['5173', '4026', '1918'],
        'commons': ['2123']
    },

    "monkey_timemachine" : {
        'AnkiDroid': ['4707', '4977'],
        'openlauncher': ['67'],
        'APhotoManager': ['116'],
        'sunflower': ['239'],
        'FirefoxLite': ['4881'],
        'collect': ['3222'],
        'WordPress': ['10302'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },

    "monkey_humandroid" :{
        'AnkiDroid': ['4707', '5756', '4977'],
        'geohashdroid': ['73'],
        'APhotoManager': ['116'],
        'collect': ['3222'],
        'WordPress': ['11135'],
        'nextcloud': ['5173', '4026', '1918'],
        'commons': ['2123'],
        'Omni-Notes': ['745']
    },

    "monkey_qtesting" :{
        'AnkiDroid': ['4451', '5756', '4977'],
        'geohashdroid': ['73'],
        'APhotoManager': ['116'],
        'WordPress': ['10302'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },

    "ape_combo" : {
        'AnkiDroid': ['5756', '4977'],
        'and-bible': ['480'],
        'geohashdroid': ['73'],
        'openlauncher': ['67'],
        'APhotoManager': ['116'],
        'AmazeFileManager': ['1796'],
        'FirefoxLite': ['4881', '5085'],
        'open-event-attendee-android': ['2198'],
        'WordPress': ['11135', '10302'],
        'nextcloud': ['5173', '4026', '1918'],
        'commons': ['2123'],
        'MaterialFBook': ['224']
    },


    "ape_timemachine": {
        'AnkiDroid': ['4707', '4977'],
        'openlauncher': ['67'],
        'APhotoManager': ['116'],
        'AmazeFileManager': ['1796'],
        'FirefoxLite': ['4881', '5085'],
        'collect': ['3222'],
        'WordPress': ['10302'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },


    "ape_humandroid":  {
        'AnkiDroid': ['4707', '5756', '4977'],
        'APhotoManager': ['116'],
        'AmazeFileManager': ['1796'],
        'FirefoxLite': ['4881', '5085'],
        'geohashdroid': ['73'],
        'open-event-attendee-android': ['2198'],
        'collect': ['3222'],
        'WordPress': ['10363'],
        'nextcloud': ['5173', '4026', '1918'],
        'commons': ['2123'],
        'Omni-Notes': ['745']
    },

    "ape_qtesting" :{
        'AnkiDroid': ['4451', '5756', '4977'],
        'geohashdroid': ['73'],
        'APhotoManager': ['116'],
        'WordPress': ['10302', '10363'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },

    "combo_timemachine":  {
        'AnkiDroid': ['4977'],
        'openlauncher': ['67'],
        'APhotoManager': ['116'],
        'AmazeFileManager': ['1796'],
        'FirefoxLite': ['4881', '5085'],
        'WordPress': ['10302'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },


    "combo_humandroid": {
        'AnkiDroid': ['5756', '4977'],
        'geohashdroid': ['73'],
        'APhotoManager': ['116'],
        'AmazeFileManager': ['1796'],
        'FirefoxLite': ['5085'],
        'open-event-attendee-android': ['2198'],
        'WordPress': ['11992', '11135'],
        'nextcloud': ['5173', '4026', '1918'],
        'commons': ['2123']
    },

    "combo_qtesting": {
        'AnkiDroid': ['5756', '4977'],
        'geohashdroid': ['73'],
        'APhotoManager': ['116'],
        'WordPress': ['10302'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },

    "timemachine_humandroid":  {
        'AnkiDroid': ['4707', '4977'],
        'APhotoManager': ['116'],
        'AmazeFileManager': ['1796'],
        'FirefoxLite': ['4942', '5085'],
        'collect': ['3222'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },

    "timemachine_qtesting": {
        'AnkiDroid': ['4977'],
        'APhotoManager': ['116'],
        'WordPress': ['10302'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    },

    "humandroid_qtesting": {
        'AnkiDroid': ['5756', '4977'],
        'geohashdroid': ['73'],
        'APhotoManager': ['116'],
        'WordPress': ['10363'],
        'nextcloud': ['5173', '4026'],
        'commons': ['2123']
    }
}


bugs_triggered_by_all_tools = ["4707", "73", "4977", "116", "10302", "5173", "4026", "2123"]


def generate_pairwise_bug_triggering_time_data(tool_names, args):

    bug_triggering_data_dict: Dict[str, List] = {}

    for tool_name in tool_names:

        file_path = os.path.join("../final_results", tool_name + ".bug.triggering.csv")
        data_file = open(file_path, 'r')
        c = csv.reader(data_file, delimiter=',')
        for row in c:
            if tool_name not in bug_triggering_data_dict:
                bug_triggering_data_dict[tool_name] = [row]
            else:
                bug_triggering_data_dict[tool_name].append(row)

    for two_tool_str in common_bugs_data:

        res = two_tool_str.split("_")
        tool_name_1 = res[0]
        tool_name_2 = res[1]

        if tool_name_1 not in bug_triggering_data_dict or tool_name_2 not in bug_triggering_data_dict:
            # check
            continue

        tool_name_1_bug_triggering_data = bug_triggering_data_dict[tool_name_1]
        tool_name_2_bug_triggering_data = bug_triggering_data_dict[tool_name_2]

        common_bugs_dict = common_bugs_data[two_tool_str]

        # collect common bug triggering data
        tool_name_1_filtered_data = []
        tool_name_2_filtered_data = []

        for app_name in common_bugs_dict:

            issue_ids = common_bugs_dict[app_name]
            for issue_id in issue_ids:

                if args.filter and issue_id in bugs_triggered_by_all_tools:
                    # filter simple bugs
                    continue

                for row in tool_name_1_bug_triggering_data:
                    if row[0] == app_name and issue_id in row[1]:
                        tool_name_1_filtered_data.append(row)

                for row in tool_name_2_bug_triggering_data:
                    if row[0] == app_name and issue_id in row[1]:
                        tool_name_2_filtered_data.append(row)

        if args.filter:
            result_file_path = os.path.join("../final_results", two_tool_str + ".nontrivial.csv")
        else:
            result_file_path = os.path.join("../final_results", two_tool_str + ".csv")
        print("write the result to: %s" % result_file_path)
        with open(result_file_path, "w") as csv_file:
            writer = csv.writer(csv_file)

            for row in tool_name_1_filtered_data:
                writer.writerow(row)

            writer.writerow(["", ""])

            for row in tool_name_2_filtered_data:
                writer.writerow(row)

        csv_file.close()


if __name__ == '__main__':

    ap = ArgumentParser()

    ap.add_argument('--filter', default=False, action='store_true',
                    help="filter trivial bugs that can be triggered by all evaluated tools (do not need to"
                         "use this option by default)")

    args = ap.parse_args()

    tool_names = ['monkey', 'ape', 'combo', 'humandroid', 'timemachine', 'qtesting']
    #tool_names = ['monkey', 'ape']
    generate_pairwise_bug_triggering_time_data(tool_names, args)
