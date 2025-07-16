# -*- coding: utf-8 -*-
"""nafas functions."""

from typing import Dict, List, Tuple
from typing import Generator, Callable, Any, Union, Optional
import time
import json
from nafas.params import NAFAS_LINKS, NAFAS_DESCRIPTION, NAFAS_TIPS, NAFAS_CAUTIONS
from nafas.params import STANDARD_MENU, STANDARD_MENU_ORDER, STEP_MAP
from nafas.params import PROGRAMS, PROGRAM_DETAILS, SOUND_MAP, STEP_TEMPLATE, CYCLE_TEMPLATE
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


def print_line(num: int = 70, char: str = "#") -> None:
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


def calculate_bpm(program_data: Dict[str, Any]) -> float:
    """
    Calculate Breaths Per Minute (BPM).

    :param program_data: program data
    """
    total_time_per_breath = sum(program_data["ratio"]) * program_data["unit"]
    bpm = round(60 / total_time_per_breath, 2)
    if is_int(bpm):
        bpm = int(bpm)
    return bpm


def calculate_time(program_data: Dict[str, Any]) -> float:
    """
    Calculate and return the program time.

    :param program_data: program data
    """
    result = sum(program_data["ratio"]) * program_data["unit"] * \
        program_data["cycle"] + program_data["pre"]
    return result


def calculate_average_time(program_data: Dict[str, Any]) -> float:
    """
    Calculate and return average time of a program in all levels.

    :param program_data: program data in all levels
    """
    result = 0
    level_number = len(program_data)
    for program in program_data.values():
        result += calculate_time(program)
    return result / level_number


def convert_time(input_time: float, average: bool = False) -> str:
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


def justify_left(words: List[str], width: int) -> str:
    """
    Left justify words.

    :param words: list of words
    :param width: width of each line
    """
    return ' '.join(words).ljust(width)


def justify_text(words: List[str], width: int) -> Generator[str, None, None]:
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
                yield justify_left(line, width)
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
        yield justify_left(line, width)


def check_sound() -> bool:
    """Check sound playing device, return True if sound device is available."""
    sound_path = get_sound_path(SOUND_MAP['Silence'])
    try:
        nava.play(sound_path)
        return True
    except Exception:
        warn(SOUND_WARNING_MESSAGE, RuntimeWarning)
        return False


def print_nafas_description() -> None:
    """Print Nafas description."""
    print(NAFAS_LINKS)
    print_line()
    print("\n".join(justify_text(NAFAS_DESCRIPTION.split(), 100)))
    print_line()
    print(NAFAS_TIPS)
    print_line()
    print(NAFAS_CAUTIONS)


def print_program_details(program_name: str, level: str, program_data: Dict[str, Any]) -> None:
    """
    Print program details.

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
    total_time = calculate_time(program_data)
    bpm = calculate_bpm(program_data)
    print_line()
    print(
        PROGRAM_DETAILS.format(
            name=program_name,
            level=level,
            cycles=str(cycle),
            unit=str(unit),
            total_time=convert_time(total_time),
            bpm=bpm,
            sequence=sequence))
    print_line()
    time.sleep(1)


def filter_input(input_data: Dict[str, Any]) -> Dict[str, Any]:
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


def get_standard_input(input_func: Callable = input) -> Dict[str, Any]:
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
                program_average_time = calculate_average_time(PROGRAMS[program_name])
                print(
                    PROGRAM_TIME_TEMPLATE.format(
                        index=i,
                        name=program_name,
                        average_time=convert_time(
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


def get_sound_path(sound_name: str, speaker_id: Optional[str] = None) -> str:
    """
    Return direct sound path.

    :param sound_name: .wav sound name
    :param speaker_id: speaker id
    """
    cd, _ = os.path.split(__file__)
    if speaker_id is None:
        return os.path.join(cd, "sounds", sound_name)
    return os.path.join(cd, "sounds", speaker_id, sound_name)


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


def run_program(program_data: Dict[str, Any], speaker_id: str, silent: bool = False) -> None:
    """
    Run program.

    :param program_data: program data
    :param speaker_id: speaker id
    :param silent: silent mode flag
    """
    check_sound_flag = False
    if not silent:
        check_sound_flag = check_sound()
    cycle = program_data["cycle"]
    ratio = program_data["ratio"]
    unit = program_data["unit"]
    pre = program_data["pre"]
    print("Preparing ", end="", flush=True)
    play_sound(get_sound_path(SOUND_MAP['Prepare'], speaker_id), enable=check_sound_flag)
    graphic_counter(pre)
    print_line()
    time.sleep(1)
    play_sound(get_sound_path(SOUND_MAP['Start'], speaker_id), enable=check_sound_flag)
    print("Start", flush=True)
    time.sleep(1)
    print_line()
    time.sleep(1)
    for i in range(cycle):
        print(CYCLE_TEMPLATE.format(cycle=str(i + 1), remaining=str(cycle - i - 1)))
        time.sleep(1)
        for index, item in enumerate(ratio):
            if item != 0:
                item_name = STEP_MAP[index]
                play_sound(get_sound_path(SOUND_MAP[item_name], speaker_id), enable=check_sound_flag)
                print(
                    STEP_TEMPLATE.format(
                        step=item_name,
                        time=str(unit * item)), flush=True)
                graphic_counter(item * unit)
        time.sleep(1)
        print_line()
    play_sound(get_sound_path(SOUND_MAP['End'], speaker_id), enable=check_sound_flag)
    print(PROGRAM_END_MESSAGE, flush=True)
    time.sleep(2)


def clear_screen() -> None:
    """Clear screen."""
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')
