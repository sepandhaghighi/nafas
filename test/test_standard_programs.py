# -*- coding: utf-8 -*-
"""Regression coverage for the additional standard breathing programs."""


def bee_breath():
    """
    Select Bee Breath at every level and skip its zero-duration phases.

    >>> import contextlib
    >>> import io
    >>> from unittest.mock import patch
    >>> from nafas.functions import calculate_bpm, calculate_time, get_program_data, run_program
    >>> name, level, data = get_program_data({"program": 21, "level": 1})
    >>> name, level
    ('Bee Breath', 'Beginner')
    >>> [get_program_data({"program": 21, "level": level})[2]["cycle"] for level in (1, 2, 3)]
    [4, 10, 20]
    >>> data["ratio"], data["unit"], data["pre"], calculate_bpm(data), calculate_time(data)
    ([5, 0, 10, 0], 1, 3, 4, 63)
    >>> output = io.StringIO()
    >>> with patch("nafas.functions.graphic_counter") as counter, patch("nafas.functions.time.sleep"), contextlib.redirect_stdout(output):
    ...     run_program(data, "us1", silent=True)
    >>> [call[0][0] for call in counter.call_args_list]
    [3, 5, 10, 5, 10, 5, 10, 5, 10]
    >>> output.getvalue().count("Cycle:"), "Retain for" in output.getvalue(), "Sustain for" in output.getvalue()
    (4, False, False)
    """


def skull_shining_breath():
    """
    Select Skull Shining Breath at every level and use one-second phases.

    >>> from nafas.functions import calculate_bpm, calculate_time, get_program_data
    >>> name, level, data = get_program_data({"program": 22, "level": 1})
    >>> name, level
    ('Skull Shining Breath', 'Beginner')
    >>> [get_program_data({"program": 22, "level": level})[2]["cycle"] for level in (1, 2, 3)]
    [10, 50, 200]
    >>> data["ratio"], data["unit"], data["pre"], calculate_bpm(data), calculate_time(data)
    ([1, 0, 1, 0], 1, 3, 30, 23)
    """


def floating_breath():
    """
    Select Floating Breath at every level, retaining but not sustaining.

    >>> import contextlib
    >>> import io
    >>> from unittest.mock import patch
    >>> from nafas.functions import calculate_bpm, calculate_time, get_program_data, run_program
    >>> name, level, data = get_program_data({"program": 23, "level": 1})
    >>> name, level
    ('Floating Breath', 'Beginner')
    >>> [get_program_data({"program": 23, "level": level})[2]["cycle"] for level in (1, 2, 3)]
    [2, 5, 10]
    >>> data["ratio"], data["unit"], data["pre"], calculate_bpm(data), calculate_time(data)
    ([8, 30, 10, 0], 1, 3, 1.25, 99)
    >>> output = io.StringIO()
    >>> with patch("nafas.functions.graphic_counter") as counter, patch("nafas.functions.time.sleep"), contextlib.redirect_stdout(output):
    ...     run_program(data, "us1", silent=True)
    >>> [call[0][0] for call in counter.call_args_list]
    [3, 8, 30, 10, 8, 30, 10]
    >>> output.getvalue().count("Cycle:"), "Retain for 30 seconds" in output.getvalue(), "Sustain for" in output.getvalue()
    (2, True, False)
    """
