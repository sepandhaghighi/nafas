# -*- coding: utf-8 -*-
"""nafas functions."""

from typing import Dict, List, Tuple
from typing import Generator, Callable, Any, Union
import time
import json
from nafas.params import NAFAS_LINKS, NAFAS_DESCRIPTION, NAFAS_TIPS, NAFAS_CAUTIONS
from nafas.params import STANDARD_MENU, STANDARD_MENU_ORDER, STEP_MAP
from nafas.params import PROGRAMS, PROGRAM_DESCRIPTION, SOUND_MAP, STEP_TEMPLATE, CYCLE_TEMPLATE
from nafas.params import SOUND_WARNING_MESSAGE, EXIT_MESSAGE, BAD_INPUT_MESSAGE, PROGRAM_END_MESSAGE
from nafas.params import MINUTES_TEMPLATE, SECONDS_TEMPLATE, PROGRAM_TIME_TEMPLATE
from nafas.params import MENU_TEMPLATE_1, MENU_TEMPLATE_2
from nafas.params import CONFIG_VALIDATION_MAP
from nafas.params import SURVEY_LINK_TEMPLATE, SURVEY_DATA_TEMPLATE
from nafas.params import NAFAS_VERSION
import nava
import os
from warnings import warn
import sys


def line(num: int = 70, char: str = "#") -> None:
    """
    Print line.

    :param num: number of characters
    :param char: character
    """
    print(num * char)


def is_int(number: Union[int, float]) -> bool:
    """
    Check that input number is int or not.

    :param number: input number
    """
    if int(number) == number:
        return True
    return False


def bpm_calc(program_data: Dict[str, Any]) -> float:
    """
    Calculate Breaths Per Minute (BPM).

    :param program_data: program data
    """
    total_time_per_breath = sum(program_data["ratio"].values()) * program_data["unit"]
    bpm = round(60 / total_time_per_breath, 2)
    if is_int(bpm):
        bpm = int(bpm)
    return bpm


def time_calc(program_data: Dict[str, Any]) -> float:
    """
    Calculate and return the program time.

    :param program_data: program data
    """
    result = sum(program_data["ratio"]) * program_data["unit"] * \
        program_data["cycle"] + program_data["pre"]
    return result


def time_average_calc(program_data: Dict[str, Any]) -> float:
    """
    Calculate and return average time of a program in all levels.

    :param program_data: program data in all levels
    """
    result = 0
    level_number = len(program_data)
    for program in program_data.values():
        result += time_calc(program)
    return result / level_number


def time_convert(input_time: float, average: bool = False) -> str:
    """
    Convert input time from sec to MM,SS format.

    :param input_time: input time in sec
    :param average: average flag
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


def get_rendered_survey_link(program_name: str, level: str, program_data: Dict[str, Any]) -> str:
    """
    Get rendered survey link.

    :param program_name: program name
    :param level: program level
    :param program_data: program data
    """
    data = SURVEY_DATA_TEMPLATE.format(
        program_name=program_name,
        level=level,
        ratio_rendered="+%5B" + ",+".join([str(item) for item in program_data['ratio']]) + "%5D",
        program_data_unit=program_data['unit'],
        program_data_pre=program_data['pre'],
        program_data_cycle=program_data['cycle'],
    )
    return SURVEY_LINK_TEMPLATE.format(data=data, version=NAFAS_VERSION)


def left_justify(words: List[str], width: int) -> str:
    """
    Left justify words.

    :param words: list of words
    :param width: width of each line
    """
    return ' '.join(words).ljust(width)


def justify(words: List[str], width: int) -> Generator[str, None, None]:
    """
    Justify input words.

    :param words: list of words
    :param width: width of each line
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


def sound_check() -> bool:
    """Check sound playing device, return True if sound device is available."""
    sound_path = get_sound_path(SOUND_MAP['Silence'])
    try:
        nava.play(sound_path)
        return True
    except Exception:
        warn(SOUND_WARNING_MESSAGE, RuntimeWarning)
        return False


def nafas_description_print() -> None:
    """Print Nafas description."""
    print(NAFAS_LINKS)
    line()
    print("\n".join(justify(NAFAS_DESCRIPTION.split(), 100)))
    line()
    print(NAFAS_TIPS)
    line()
    print(NAFAS_CAUTIONS)


def program_description_print(program_name: str, level: str, program_data: Dict[str, Any]) -> None:
    """
    Print program description.

    :param program_name: program name
    :param level: program level
    :param program_data: program data
    """
    cycle = program_data["cycle"]
    ratio = program_data["ratio"]
    unit = program_data["unit"]
    sequence = []
    for index, item in enumerate(ratio):
        sequence.append("{step}({ratio})".format(step=STEP_MAP[index], ratio=item))
    sequence = ", ".join(sequence)
    total_time = time_calc(program_data)
    bpm = bpm_calc(program_data)
    line()
    print(
        PROGRAM_DESCRIPTION.format(
            name=program_name,
            level=level,
            cycles=str(cycle),
            unit=str(unit),
            total_time=time_convert(total_time),
            bpm=bpm,
            sequence=sequence))
    line()
    time.sleep(1)


def input_filter(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Filter input data.

    :param input_data: input data
    """
    filtered_data = input_data.copy()
    if filtered_data["program"] not in STANDARD_MENU["program"]:
        filtered_data["program"] = 1
    if filtered_data["level"] not in STANDARD_MENU["level"]:
        filtered_data["level"] = 1
    return filtered_data


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.

    :param config_path: config path
    """
    try:
        with open(config_path, 'r') as config_file:
            config_data = json.load(config_file)
        if not validate_config(config_data):
            raise Exception
        program_data = {
            'ratio': [
                config_data['ratio']['inhale'],
                config_data['ratio']['retain'],
                config_data['ratio']['exhale'],
                config_data['ratio']['sustain']
            ],
            'unit': config_data['unit'],
            'pre': config_data['pre'],
            'cycle': config_data['cycle'],
        }
        return {
            "status": True,
            "data": {
                "program_name": config_data['name'],
                "program_level": "Custom",
                "program_data": program_data
            }
        }
    except Exception:
        return {"status": False, "data": dict()}


def validate_config(config_data: Dict[str, Any]) -> bool:
    """
    Validate config data. Return True if config data is valid.

    :param config_data: config data
    """
    result = []
    for item1 in CONFIG_VALIDATION_MAP:
        if item1 not in config_data:
            return False
        if isinstance(CONFIG_VALIDATION_MAP[item1], dict):
            for item2 in CONFIG_VALIDATION_MAP[item1]:
                if item2 not in config_data[item1]:
                    return False
                result.append(isinstance(config_data[item1][item2], CONFIG_VALIDATION_MAP[item1][item2]))
        else:
            result.append(isinstance(config_data[item1], CONFIG_VALIDATION_MAP[item1]))
    return all(result)


def get_input_standard(input_func: Callable = input) -> Dict[str, Any]:
    """
    Get inputs from user.

    :param input_func : input function
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


def get_program_data(input_data: Dict[str, Any]) -> Tuple:
    """
    Get program data as program name, level and program data.

    :param input_data: input data
    """
    program_name = STANDARD_MENU["program"][input_data["program"]]
    level = STANDARD_MENU["level"][input_data["level"]]
    return program_name, level, PROGRAMS[program_name][level]


def get_sound_path(sound_name: str) -> str:
    """
    Return direct sound path.

    :param sound_name: .wav sound name
    """
    cd, _ = os.path.split(__file__)
    return os.path.join(cd, "sounds", sound_name)


def graphic_counter(delay_time: float) -> None:
    """
    Print dots during cycles.

    :param delay_time: delay time
    """
    for _ in range(int(delay_time)):
        time.sleep(1)
        print('.', end=' ', flush=True)
    remain_time = delay_time - int(delay_time)
    time.sleep(remain_time)
    if remain_time != 0:
        print('.', end=' ', flush=True)
    print("")


def play_sound(sound_path: str, enable: bool = True) -> None:
    """
    Play inputted sound file.

    :param sound_path: sound path
    :param enable: enable flag
    """
    if enable:
        _ = nava.play(sound_path, async_mode=True)


def run(program_data: Dict[str, Any], silent: bool = False) -> None:
    """
    Run program.

    :param program_data: program data
    :param silent: silent mode flag
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


def clear_screen() -> None:
    """Clear screen."""
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
