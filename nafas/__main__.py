# -*- coding: utf-8 -*-
"""nafas main."""

import sys
import webbrowser
import argparse
from nafas.functions import print_nafas_description, get_standard_input, filter_input
from nafas.functions import get_program_data, print_program_details, run_program, clear_screen
from nafas.functions import load_config, get_rendered_survey_link, print_line
from nafas.params import NAFAS_VERSION, EXIT_MESSAGE
from nafas.params import CONFIG_LOAD_ERROR_MESSAGE, SURVEY_MESSAGE_1, SURVEY_MESSAGE_2
from nafas.params import SPEAKER_LIST
from art import tprint


def main() -> None:
    """CLI main function."""
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--version', help='version', nargs="?", const=1)
        parser.add_argument('--silent', help='silent mode', nargs="?", const=1)
        parser.add_argument('--skip-intro', help='skip intro', nargs="?", const=1)
        parser.add_argument('--config', help='path to the configuration file', type=str)
        parser.add_argument(
            '--speaker',
            help='speaker id',
            choices=SPEAKER_LIST,
            default=SPEAKER_LIST[0],
            type=str.lower)
        args = parser.parse_args()
        silent_flag = args.silent
        if args.version:
            print(NAFAS_VERSION)
        else:
            if not args.skip_intro:
                tprint("Nafas")
                tprint("v" + str(NAFAS_VERSION))
                if silent_flag:
                    tprint("Silent Mode")
                print_nafas_description()
                _ = input("Press any key to continue.\n")
            EXIT_FLAG = False
            while not EXIT_FLAG:
                if args.config:
                    result = load_config(args.config)
                    if result["status"]:
                        data = result["data"]
                        program_name, level, program_data = data["program_name"], data["program_level"], data["program_data"]
                    else:
                        print(CONFIG_LOAD_ERROR_MESSAGE)
                        sys.exit()
                else:
                    input_data = get_standard_input()
                    filtered_data = filter_input(input_data)
                    program_name, level, program_data = get_program_data(filtered_data)
                clear_screen()
                print_program_details(program_name, level, program_data)
                run_program(program_data, args.speaker, silent=silent_flag)
                print_line()
                survey_link = get_rendered_survey_link(program_name, level, program_data)
                print(SURVEY_MESSAGE_1)
                print("Survey Link: {link}\n".format(link=survey_link))
                if input(SURVEY_MESSAGE_2).lower() == "y":
                    webbrowser.open(survey_link)
                INPUTINDEX = str(
                    input("Press [R] to restart or any other key to exit."))
                if INPUTINDEX.upper() != "R":
                    EXIT_FLAG = True
                    print(EXIT_MESSAGE)
                else:
                    clear_screen()
    except (KeyboardInterrupt, EOFError):
        print("\n" + EXIT_MESSAGE)


if __name__ == "__main__":
    main()
