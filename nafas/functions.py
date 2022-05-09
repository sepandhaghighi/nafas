# -*- coding: utf-8 -*-
"""nafas functions."""

import time
from nafas.params import NAFAS_DESCRIPTION, NAFAS_NOTICE, STANDARD_MENU, STANDARD_MENU_ORDER, STEP_MAP
from nafas.params import PROGRAMS, PROGRAM_DESCRIPTION, SOUND_MAP, SOUND_ERROR_MESSAGE, STEP_TEMPLATE, CYCLE_TEMPLATE
import playsound
import threading
import os


def line(num=70, char="#"):
    """
    Print line.

    :param num: number of characters
    :type num: int
    :param char: character
    :type char: str
    :return: None
    """
    print(num * char)


def time_calc(program_data):
    """
    Calculate program time.

    :param program_data: program data
    :type program_data: dict
    :return: time as float
    """
    result = sum(program_data["ratio"]) * program_data["unit"] * \
        program_data["cycle"] + program_data["pre"]
    return result


def time_average_calc(program_data):
    """
    Calculate average time of a program in all levels.

    :param program_data: program data in all levels
    :type program_data: dict
    :return: average time as float
    """
    result = 0
    level_number = len(program_data)
    for program in program_data.values():
        result += time_calc(program)
    return result / level_number


def time_convert(input_time, average=False):
    """
    Convert input time from sec to MM,SS format.

    :param input_time: input time in sec
    :type input_time: float
    :param average: average flag
    :type average: bool
    :return: converted time as str
    """
    sec = float(input_time)
    _days, sec = divmod(sec, 24 * 3600)
    _hours, sec = divmod(sec, 3600)
    minutes, sec = divmod(sec, 60)
    result = ", ".join([
        "{:02.0f} minutes".format(minutes),
        "{:02.0f} seconds".format(sec),
    ])
    if average:
        if sec >= 30:
            minutes += 1
        result = "{:02.0f} minutes".format(minutes).lstrip("0")
    return result


def left_justify(words, width):
    """
    Left justify words.

    :param words: list of words
    :type words : list
    :param width: width of each line
    :type width: int
    :return: left justified words as list
    """
    return ' '.join(words).ljust(width)


def justify(words, width):
    """
    Justify input words.

    :param words: list of words
    :type words : list
    :param width: width of each line
    :type width : int
    :return: list of justified words as list
    """
    line = []
    col = 0
    for word in words:
        if line and col + len(word) > width:
            if len(line) == 1:
                yield left_justify(line, width)
            else:
                # After n + 1 spaces are placed between each pair of
                # words, there are r spaces left over; these result in
                # wider spaces at the left.
                n, r = divmod(width - col + 1, len(line) - 1)
                narrow = ' ' * (n + 1)
                if r == 0:
                    yield narrow.join(line)
                else:
                    wide = ' ' * (n + 2)
                    yield wide.join(line[:r] + [narrow.join(line[r:])])
            line, col = [], 0
        line.append(word)
        col += len(word) + 1
    if line:
        yield left_justify(line, width)


def description_print():
    """
    Print description.

    :return: None
    """
    print("\n".join(justify(NAFAS_DESCRIPTION.split(), 100)))
    print(NAFAS_NOTICE)


def program_description_print(program_name, level, program_data):
    """
    Print program description.

    :param program_name: program name
    :type program_name: str
    :param level: program level
    :type level: str
    :param program_data: program data
    :type program_data: dict
    :return: None
    """
    cycle = program_data["cycle"]
    ratio = program_data["ratio"]
    sequence = []
    for index, item in enumerate(ratio):
        if item != 0:
            sequence.append(STEP_MAP[index])
    sequence = ", ".join(sequence)
    total_time = time_calc(program_data)
    line()
    print(
        PROGRAM_DESCRIPTION.format(
            program_name,
            level,
            str(cycle),
            time_convert(total_time),
            sequence))
    line()
    time.sleep(1)


def input_filter(input_data):
    """
    Filter input data.

    :param input_data: input data
    :type input_data: dict
    :return: filtered data as dict
    """
    filtered_data = input_data.copy()
    if filtered_data["program"] not in STANDARD_MENU["program"].keys():
        filtered_data["program"] = 1
    if filtered_data["level"] not in STANDARD_MENU["level"].keys():
        filtered_data["level"] = 1
    return filtered_data


def get_input_standard(input_func=input):
    """
    Get inputs from user.

    :param input_func : input function
    :type input_func : function object
    :return: input data as dict
    """
    input_data = {"program": 1, "level": 1}
    for item in STANDARD_MENU_ORDER:
        exit_flag = False
        sorted_list = sorted(list(STANDARD_MENU[item].keys()))
        print("- Please choose a {0} : \n".format(item))
        for i in sorted_list:
            if item == "program":
                program_name = STANDARD_MENU[item][i]
                program_average_time = time_average_calc(
                    PROGRAMS[program_name])
                print(
                    str(i) +
                    "- " +
                    program_name +
                    " (~ " +
                    time_convert(
                        program_average_time,
                        True) +
                    ")")
            else:
                print(str(i) + "- " + STANDARD_MENU[item][i])
        while not exit_flag:
            try:
                input_data[item] = int(input_func(""))
                exit_flag = True
            except Exception:
                print("[Error] Bad Input!")
    return input_data


def get_program_data(input_data):
    """
    Get program data.

    :param input_data: input data
    :type input_data: dict
    :return: program name, level and program data as tuple
    """
    program_name = STANDARD_MENU["program"][input_data["program"]]
    level = STANDARD_MENU["level"][input_data["level"]]
    return program_name, level, PROGRAMS[program_name][level]


def get_sound_path(sound_name):
    """
    Return sound path.

    :param sound_name: .wav sound name
    :type sound_name: str
    :return: direct path to sound
    """
    cd, _ = os.path.split(__file__)
    return os.path.join(cd, "sounds", sound_name)


def graphic_counter(delay_time):
    """
    Print dots during cycles.

    :param delay_time: delay time
    :type delay_time: float
    :return: None
    """
    for _ in range(int(delay_time)):
        time.sleep(1)
        print('.', end=' ', flush=True)
    remain_time = delay_time - int(delay_time)
    time.sleep(remain_time)
    if remain_time != 0:
        print('.', end=' ', flush=True)
    print()


def _playsound_async(sound_path, debug):
    """
    Play sound asynchronous in a thread.

    :param sound_path: sound path
    :type sound_path: str
    :param debug: debug mode flag
    :type debug: bool
    :return: None
    """
    try:
        playsound.playsound(sound_path)
    except Exception:
        if debug:
            print(SOUND_ERROR_MESSAGE)


def play_sound(sound_path, debug=False):
    """
    Play inputted sound file.

    :param sound_path: sound path
    :type sound_path: str
    :param debug: debug mode flag
    :type debug: bool
    :return: new thread as threading.Thread object
    """
    new_thread = threading.Thread(
        target=_playsound_async, args=(
            sound_path, debug,), daemon=True)
    new_thread.start()
    return new_thread


def run(program_data):
    """
    Run program.

    :param program_data: program data
    :type program_data: dict
    :return: None
    """
    cycle = program_data["cycle"]
    ratio = program_data["ratio"]
    unit = program_data["unit"]
    pre = program_data["pre"]
    print("Preparing ", end="", flush=True)
    sound_thread = play_sound(get_sound_path(SOUND_MAP['Prepare']))
    graphic_counter(pre)
    line()
    time.sleep(1)
    sound_thread.join()
    sound_thread = play_sound(get_sound_path(SOUND_MAP['Start']))
    print("Start", flush=True)
    time.sleep(1)
    sound_thread.join()
    line()
    time.sleep(1)
    for i in range(cycle):
        print(CYCLE_TEMPLATE.format(str(i + 1), str(cycle - i - 1)))
        time.sleep(1)
        for index, item in enumerate(ratio):
            if item != 0:
                item_name = STEP_MAP[index]
                sound_thread = play_sound(get_sound_path(SOUND_MAP[item_name]))
                print(
                    STEP_TEMPLATE.format(
                        item_name, str(
                            unit * item)), flush=True)
                graphic_counter(item * unit)
                sound_thread.join()
        time.sleep(1)
        line()
    sound_thread = play_sound(get_sound_path(SOUND_MAP['End']))
    print("Well done!", flush=True)
    sound_thread.join()
