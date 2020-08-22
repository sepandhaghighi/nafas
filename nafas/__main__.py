# -*- coding: utf-8 -*-
"""nafas main."""

from .functions import *

if __name__ == "__main__":
    input_data = get_input_standard()
    filtered_data = input_filter(input_data)
    program_data = get_program_dict(filtered_data)
    run(program_data)