# -*- coding: utf-8 -*-
"""nafas functions."""

import time
from .params import DESCRIPTION, STANDARD_MENU, STEP_MAP, PROGRAMS


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


def input_filter(input_dict):
    """
    Filter input data.

    :param input_dict: input data
    :type input_dict: dict
    :return: filtered data as dict
    """
    filtered_dict = input_dict.copy()
    if filtered_dict["program"] not in STANDARD_MENU["program"].keys():
        filtered_dict["program"] = 1
    if filtered_dict["level"] not in STANDARD_MENU["level"].keys():
        filtered_dict["level"] = 1
    return filtered_dict


def get_input_standard(input_func=input):
    """
    Get inputs from user.

    :param input_func : input function
    :type input_func : function object
    :return: input data as dict
    """
    input_dict = {"program": 1, "level": 1}
    for item in sorted(STANDARD_MENU.keys()):
        exit_flag = False
        sorted_list = sorted(list(STANDARD_MENU[item].keys()))
        print("- Please choose a {0} : ".format(item))
        for i in sorted_list:
            print(str(i) + "- " + STANDARD_MENU[item][i])
        while not exit_flag:
            try:
                input_dict[item] = int(input_func(""))
                exit_flag = True
            except Exception:
                print("[Error] Bad Input!")
    return input_dict


def get_program_dict(input_dict):
    """
    Get program dictionary.

    :param input_dict: input data
    :type input_dict: dict
    :return: program data as dict
    """
    program_name = STANDARD_MENU["program"][input_dict["program"]]
    level = STANDARD_MENU["level"][input_dict["level"]]
    return PROGRAMS[program_name][level]


def run(program_dict):
    """
    Run program.

    :param program_dict: program data
    :type program_dict: dict
    :return: None
    """
    cycle = program_dict["cycle"]
    ratio = program_dict["ratio"]
    unit = program_dict["unit"]
    pre = program_dict["pre"]
    print("Preparing . . .")
    for i in range(pre):
        print(i + 1)
        time.sleep(unit)
    line()
    print("Start")
    line()
    for i in range(cycle):
        print("Cycle : " + str(i + 1))
        for index, item in enumerate(ratio):
            if item != 0:
                print(
                    "- " +
                    STEP_MAP[index] +
                    " for {0} sec".format(
                        unit *
                        item))
                time.sleep(unit * item)
        line()
    print("End!")
