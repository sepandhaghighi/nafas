# -*- coding: utf-8 -*-
"""nafas main."""

import argparse
from nafas.functions import description_print, get_input_standard, input_filter
from nafas.functions import get_program_data, program_description_print, run
from nafas.params import NAFAS_VERSION
from art import tprint


def main():
    """
    CLI main function.

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help='version', nargs="?", const=1)
    args = parser.parse_args()
    if args.version:
        print(NAFAS_VERSION)
    else:
        tprint("Nafas")
        tprint("v" + str(NAFAS_VERSION))
        description_print()
        EXIT_FLAG = False
        while not EXIT_FLAG:
            input_data = get_input_standard()
            filtered_data = input_filter(input_data)
            program_name, level, program_data = get_program_data(filtered_data)
            program_description_print(program_name, level, program_data)
            run(program_data)
            INPUTINDEX = str(
                input("Press [R] to restart or any other key to exit."))
            if INPUTINDEX.upper() != "R":
                EXIT_FLAG = True



if __name__ == "__main__":
    main()
