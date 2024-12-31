# -*- coding: utf-8 -*-
"""nafas main."""

import argparse
from nafas.functions import description_print, get_input_standard, input_filter
from nafas.functions import get_program_data, program_description_print, run, clear_screen
from nafas.params import NAFAS_VERSION, EXIT_MESSAGE
from art import tprint


def main():
    """
    CLI main function.

    :return:
    """
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--version', help='version', nargs="?", const=1)
        parser.add_argument('--silent', help='silent mode', nargs="?", const=1)
        args = parser.parse_args()
        silent_flag = args.silent
        if args.version:
            print(NAFAS_VERSION)
        else:
            tprint("Nafas")
            tprint("v" + str(NAFAS_VERSION))
            if silent_flag:
                tprint("Silent Mode")
            description_print()
            _ = input("Press any key to continue.")
            clear_screen()
            EXIT_FLAG = False
            while not EXIT_FLAG:
                input_data = get_input_standard()
                filtered_data = input_filter(input_data)
                program_name, level, program_data = get_program_data(filtered_data)
                clear_screen()
                program_description_print(program_name, level, program_data)
                run(program_data, silent=silent_flag)
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
