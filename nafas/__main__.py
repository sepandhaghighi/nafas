# -*- coding: utf-8 -*-
"""nafas main."""

import sys
from .functions import *
from art import tprint
from .params import NAFAS_VERSION

if __name__ == "__main__":
    args = sys.argv
    tprint("Nafas")
    tprint("v" + str(NAFAS_VERSION))
    if len(args) > 1:
        if args[1].upper() == "TEST":
            description_print(lambda x : "1")
    else:
        description_print()
    input_data = get_input_standard()
    filtered_data = input_filter(input_data)
    program_data = get_program_dict(filtered_data)
    run(program_data)