# -*- coding: utf-8 -*-
"""nafas functions."""

import time
from .params import *

def line(num=70,char="#"):
    """
    Print line.

    :param num: number of characters
    :type num: int
    :param char: character
    :type char: str
    :return: None
    """
    print(num*char)

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
        filtered_dict["program"] = 1
    return filtered_dict

def get_input_standard():
    """
    Get inputs from user.

    :return: input data as dict
    """
    input_dict = {"program":1,"level":1}
    for item in sorted(STANDARD_MENU.keys()):
        exit_flag = False
        sorted_list = sorted(list(STANDARD_MENU[item].keys()))
        print("- Please choose a {0} : ".format(item))
        for i in sorted_list:
            print(str(i)+"- "+STANDARD_MENU[item][i])
        while not exit_flag:
            try:
                input_dict[item] = int(input(""))
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
        print(i+1)
        time.sleep(unit)
    line()
    print("Start")
    line()
    for i in range(cycle):
        print("Cycle : "+str(i+1))
        for index, item in enumerate(ratio):
            if item != 0 :
                print("- " + STEP_MAP[index]+ " for {0} sec".format(unit * item))
                time.sleep(unit * item)
        line()
    print("End!")




