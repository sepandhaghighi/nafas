# -*- coding: utf-8 -*-
"""nafas functions."""

import time
from nafas.params import NAFAS_LINKS, NAFAS_DESCRIPTION, NAFAS_TIPS, NAFAS_CAUTIONS
from nafas.params import STANDARD_MENU, STANDARD_MENU_ORDER, STEP_MAP
from nafas.params import PROGRAMS, PROGRAM_DESCRIPTION, SOUND_MAP, STEP_TEMPLATE, CYCLE_TEMPLATE
from nafas.params import SOUND_WARNING_MESSAGE, EXIT_MESSAGE, BAD_INPUT_MESSAGE, PROGRAM_END_MESSAGE
from nafas.params import MINUTES_TEMPLATE, SECONDS_TEMPLATE, PROGRAM_TIME_TEMPLATE
from nafas.params import MENU_TEMPLATE_1, MENU_TEMPLATE_2
import nava
import os
from warnings import warn
import sys


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
        MINUTES_TEMPLATE.format(minutes=minutes),
        SECONDS_TEMPLATE.format(seconds=sec),
    ])
    if average:
        if sec >= 30:
            minutes += 1
        result = MINUTES_TEMPLATE.format(minutes=minutes).lstrip("0")
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


def sound_check():
    """
    Check sound playing device.

    :return: result as bool
    """
    sound_path = get_sound_path(SOUND_MAP['Silence'])
    try:
        nava.play(sound_path)
        return True
    except Exception:
        warn(SOUND_WARNING_MESSAGE, RuntimeWarning)
        return False


def description_print():
    """
    Print description.

    :return: None
    """
    print(NAFAS_LINKS)
    line()
    print("\n".join(justify(NAFAS_DESCRIPTION.split(), 100)))
    line()
    print(NAFAS_TIPS)
    line()
    print(NAFAS_CAUTIONS)


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
    sequence = []
    for index, item in enumerate(ratio):
        sequence.append("{step}({ratio})".format(step=STEP_MAP[index], ratio=item))
    sequence = ", ".join(sequence)
    total_time = time_calc(program_data)
    line()
    print(
        PROGRAM_DESCRIPTION.format(
            name=program_name,
            level=level,
            cycles=str(cycle),
            unit=str(unit),
            total_time=time_convert(total_time),
            sequence=sequence))
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
    if filtered_data["program"] not in STANDARD_MENU["program"]:
        filtered_data["program"] = 1
    if filtered_data["level"] not in STANDARD_MENU["level"]:
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
        sorted_list = sorted(STANDARD_MENU[item])
        print(MENU_TEMPLATE_1.format(item=item))
        for i in sorted_list:
            if item == "program":
                program_name = STANDARD_MENU[item][i]
                program_average_time = time_average_calc(PROGRAMS[program_name])
                print(
                    PROGRAM_TIME_TEMPLATE.format(
                        index=i,
                        name=program_name,
                        average_time=time_convert(
                            program_average_time,
                            True)))
            else:
                print(MENU_TEMPLATE_2.format(index=i, item=STANDARD_MENU[item][i]))
        while not exit_flag:
            try:
                input_data[item] = int(input_func(""))
                exit_flag = True
            except (KeyboardInterrupt, EOFError):
                print("\n" + EXIT_MESSAGE)
                sys.exit()
            except Exception:
                print(BAD_INPUT_MESSAGE)
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
    print("")


def play_sound(sound_path, enable=True):
    """
    Play inputted sound file.

    :param sound_path: sound path
    :type sound_path: str
    :param enable: enable flag
    :type enable: bool
    :return: None
    """
    if enable:
        _ = nava.play(sound_path, async_mode=True)


def run(program_data, silent=False):
    """
    Run program.

    :param program_data: program data
    :type program_data: dict
    :param silent: silent mode flag
    :type silent: bool
    :return: None
    """
    sound_check_flag = False
    if not silent:
        sound_check_flag = sound_check()
    cycle = program_data["cycle"]
    ratio = program_data["ratio"]
    unit = program_data["unit"]
    pre = program_data["pre"]
    print("Preparing ", end="", flush=True)
    play_sound(get_sound_path(SOUND_MAP['Prepare']), enable=sound_check_flag)
    graphic_counter(pre)
    line()
    time.sleep(1)
    play_sound(get_sound_path(SOUND_MAP['Start']), enable=sound_check_flag)
    print("Start", flush=True)
    time.sleep(1)
    line()
    time.sleep(1)
    for i in range(cycle):
        print(CYCLE_TEMPLATE.format(cycle=str(i + 1), remaining=str(cycle - i - 1)))
        time.sleep(1)
        for index, item in enumerate(ratio):
            if item != 0:
                item_name = STEP_MAP[index]
                play_sound(get_sound_path(SOUND_MAP[item_name]), enable=sound_check_flag)
                print(
                    STEP_TEMPLATE.format(
                        step=item_name,
                        time=str(unit * item)), flush=True)
                graphic_counter(item * unit)
        time.sleep(1)
        line()
    play_sound(get_sound_path(SOUND_MAP['End']), enable=sound_check_flag)
    print(PROGRAM_END_MESSAGE, flush=True)
    time.sleep(2)


def clear_screen():
    """
    Clear screen.

    :return: None
    """
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
