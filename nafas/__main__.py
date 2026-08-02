# -*- coding: utf-8 -*-
"""nafas main."""

import sys
import webbrowser
import argparse
from nafas.functions import print_nafas_description, get_standard_input, filter_input
from nafas.functions import get_program_data, print_program_details, run_program, clear_screen
from nafas.functions import generate_config, load_config, get_rendered_survey_link, print_line
from nafas.functions import set_color, set_bg_color, set_intensity
from nafas.functions import unpack_program_data
from nafas.params import NAFAS_VERSION, EXIT_MESSAGE
from nafas.params import CONFIG_GENERATE_SUCCESS_MESSAGE, CONFIG_GENERATE_ERROR_MESSAGE, CONFIG_LOAD_ERROR_MESSAGE
from nafas.params import SURVEY_MESSAGE_1, SURVEY_MESSAGE_2
from nafas.params import SPEAKER_LIST, COLOR_LIST, INTENSITY_LIST
from art import tprint


def parse_args() -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help='version', nargs="?", const=1)
    parser.add_argument('--silent', help='silent mode', nargs="?", const=1)
    parser.add_argument('--skip-intro', help='skip intro', nargs="?", const=1)
    parser.add_argument(
        '--generate-config',
        help='generate a starter configuration file at the given path',
        type=str)
    parser.add_argument('--config', help='load an existing configuration file from the given path', type=str)
    parser.add_argument(
        '--speaker',
        help='speaker id',
        choices=SPEAKER_LIST,
        default=SPEAKER_LIST[0],
        type=str.lower)
    parser.add_argument('--color', help='text color', type=str.lower, choices=COLOR_LIST)
    parser.add_argument('--bg-color', help='background color', type=str.lower, choices=COLOR_LIST)
    parser.add_argument('--intensity', help='text intensity', type=str.lower, choices=INTENSITY_LIST)
    args = parser.parse_args()
    return args


def run(args: argparse.Namespace) -> None:
    """
    Run nafas CLI.

    :param args: arguments
    """
    set_color(args.color)
    set_bg_color(args.bg_color)
    set_intensity(args.intensity)
    silent_flag = args.silent
    if args.version:
        print(NAFAS_VERSION)
    elif args.generate_config:
        result = generate_config(args.generate_config)
        if not result:
            print(CONFIG_GENERATE_ERROR_MESSAGE)
        else:
            print(CONFIG_GENERATE_SUCCESS_MESSAGE)
        sys.exit()
    else:
        clear_screen()
        if not args.skip_intro:
            tprint("Nafas")
            tprint("v" + str(NAFAS_VERSION))
            if silent_flag:
                tprint("Silent Mode")
            print_nafas_description()
            _ = input("Press any key to continue.\n")
        exit_flag = False
        while not exit_flag:
            if args.config:
                result = load_config(args.config)
                if result["status"]:
                    program_name, program_level, program_data = unpack_program_data(result["data"])
                else:
                    print(CONFIG_LOAD_ERROR_MESSAGE)
                    sys.exit()
            else:
                input_data = get_standard_input()
                filtered_data = filter_input(input_data)
                program_name, program_level, program_data = get_program_data(filtered_data)
            clear_screen()
            print_program_details(program_name, program_level, program_data)
            run_program(program_data, args.speaker, silent=silent_flag)
            print_line()
            survey_link = get_rendered_survey_link(program_name, program_level, program_data)
            print(SURVEY_MESSAGE_1)
            print("Survey Link: {link}\n".format(link=survey_link))
            if input(SURVEY_MESSAGE_2).lower() == "y":
                webbrowser.open(survey_link)
            INPUTINDEX = str(
                input("Press [R] to restart or any other key to exit."))
            if INPUTINDEX.upper() != "R":
                exit_flag = True
                print(EXIT_MESSAGE)
            else:
                clear_screen()


def main() -> None:
    """CLI main function."""
    try:
        args = parse_args()
        run(args)
    except (KeyboardInterrupt, EOFError):
        print(EXIT_MESSAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
