# -*- coding: utf-8 -*-
"""nafas main."""

import sys
from nafas.functions import description_print, get_input_standard, input_filter, get_program_data, program_description_print, run
from nafas.params import NAFAS_VERSION
from art import tprint

if __name__ == "__main__":
    args = sys.argv
    tprint("Nafas")
    tprint("v" + str(NAFAS_VERSION))
    description_print()
    if len(args) < 2:
        input_data = get_input_standard()
        filtered_data = input_filter(input_data)
        program_name, level, program_data = get_program_data(filtered_data)
        program_description_print(program_name, level, program_data)
        run(program_data)
