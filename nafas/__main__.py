# -*- coding: utf-8 -*-
"""nafas main."""

from .functions import *
from art import tprint
from .params import NAFAS_VERSION

if __name__ == "__main__":

    tprint("Nafas")
    tprint("v" + str(NAFAS_VERSION))
    input_data = get_input_standard()
    filtered_data = input_filter(input_data)
    program_data = get_program_dict(filtered_data)
    run(program_data)