# -*- coding: utf-8 -*-
"""nafas functions."""

import time
from nafas.params import DESCRIPTION, STANDARD_MENU, STEP_MAP, PROGRAMS, PROGRAM_DESCRIPTION, SOUND_MAP, SOUND_ERROR_MESSAGE
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


def time_convert(input_time):
    """
    Convert input time from sec to MM,SS format.

    :param input_time: input time in sec
    :type input_time: float
    :return: converted time as str
    """
    sec = float(input_time)
    _days, sec = divmod(sec, 24 * 3600)
    _hours, sec = divmod(sec, 3600)
    minutes, sec = divmod(sec, 60)
    return ", ".join([
        "{:02.0f} minutes".format(minutes),
        "{:02.0f} seconds".format(sec),
    ])


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
    print("\n".join(justify(DESCRIPTION.split(), 100)))
    print("\n")


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
    unit = program_data["unit"]
    pre = program_data["pre"]
    unit_time = 0
    sequence = []
    for index, item in enumerate(ratio):
        unit_time += item * unit
        if item != 0:
            sequence.append(STEP_MAP[index])
    sequence = ", ".join(sequence)
    total_time = (unit_time * cycle) + pre
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
    for item in sorted(STANDARD_MENU.keys()):
        exit_flag = False
        sorted_list = sorted(list(STANDARD_MENU[item].keys()))
        print("- Please choose a {0} : ".format(item))
        for i in sorted_list:
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
    print("Preparing ", end="")
    graphic_counter(pre)
    line()
    time.sleep(unit / 2)
    print("Start")
    time.sleep(unit / 2)
    line()
    time.sleep(unit / 2)
    for i in range(cycle):
        print("Cycle : " + str(i + 1))
        time.sleep(unit / 2)
        for index, item in enumerate(ratio):
            if item != 0:
                item_name = STEP_MAP[index]
                sound_thread = play_sound(get_sound_path(SOUND_MAP[item_name]))
                print(
                    "- " +
                    item_name +
                    " for {0} sec".format(
                        unit *
                        item))
                graphic_counter(item * unit)
                sound_thread.join()
        time.sleep(1)
        line()
    print("End!")
