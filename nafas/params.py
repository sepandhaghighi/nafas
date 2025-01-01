# -*- coding: utf-8 -*-
"""nafas parameters."""

NAFAS_VERSION = "0.8"

NAFAS_DESCRIPTION = """
Breathing gymnastics is a system of breathing exercises that focuses on the treatment of various diseases and general health promotion.
Nafas is a collection of breathing gymnastics designed to reduce the exhaustion of long working hours.
With multiple breathing patterns, Nafas helps you find your way to a detoxified energetic workday and also improves your concentration by increasing the oxygen level.
No need to walk away to take a break, just sit comfortably, run Nafas and let the journey begin.
"""

NAFAS_LINKS = """
Repository: https://github.com/sepandhaghighi/nafas
Paper: https://arxiv.org/abs/2412.04667
* If you use Nafas in your research, please cite our paper
"""

NAFAS_TIPS = """
Breathing tips:

1. Inhaling is only done through the nose
2. Exhaling, you can use both nose and mouth
3. When exhaling through your mouth, it is recommended to fold the lips
"""

NAFAS_CAUTIONS = """
Cautions:

1. If you have any breathing or respiratory issues, consult your doctor before using Nafas
2. If you have asthma or high blood pressure should not hold the breath
3. If you feel dizzy, nauseous, or lightheaded stop practicing and rest
"""

SOUND_WARNING_MESSAGE = "Your device is not compatible with our underlying sound-playing library. You can refer to https://github.com/openscilab/nava."

EXIT_MESSAGE = "See you. Bye!"

BAD_INPUT_MESSAGE = "[Error] Bad input!"

PROGRAM_END_MESSAGE = "Well done!"

PROGRAM_DESCRIPTION = """Program details:

Name             : {0}

Level            : {1}

Number of Cycles : {2}

Unit             : {3} seconds

Total Time       : {4}

Sequence         : {5}
"""

MINUTES_TEMPLATE = "{:02.0f} minutes"

SECONDS_TEMPLATE = "{:02.0f} seconds"

PROGRAM_TIME_TEMPLATE = "{0}- {1} (~ {2})"

MENU_TEMPLATE_1 = "- Choose a {0}: \n"

MENU_TEMPLATE_2 = "{0}- {1}"

CYCLE_TEMPLATE = "Cycle: {0} (Remaining: {1})"

STEP_TEMPLATE = "- {0} for {1} seconds"

STANDARD_MENU = {
    "program": {
        1: "Clear Mind",
        2: "Relax1",
        3: "Relax2",
        4: "Relax3",
        5: "Calming1",
        6: "Calming2",
        7: "Power",
        8: "Harmony",
        9: "Anti-Stress",
        10: "Anti-Appetite",
        11: "Cigarette Replace",
        12: "Decision-Making",
        13: "Balancing",
        14: "Energizing"},
    "level": {
        1: "Beginner",
        2: "Medium",
        3: "Advanced"}}

STANDARD_MENU_ORDER = ["program", "level"]

STEP_MAP = {0: "Inhale", 1: "Retain", 2: "Exhale", 3: "Sustain"}

CLEAR_MIND_BEGINNER = {"ratio": [1, 0, 3, 0], "unit": 3, "pre": 3, "cycle": 35}

CLEAR_MIND_MEDIUM = {"ratio": [1, 0, 4, 0], "unit": 3, "pre": 3, "cycle": 28}

CLEAR_MIND_ADVANCED = {"ratio": [1, 0, 5, 0], "unit": 3, "pre": 3, "cycle": 24}

RELAX_BEGINNER = {"ratio": [1, 0, 2, 2], "unit": 3, "pre": 3, "cycle": 28}

RELAX_MEDIUM = {"ratio": [1, 0, 2, 3], "unit": 3, "pre": 3, "cycle": 24}

RELAX_ADVANCED = {"ratio": [1, 0, 2, 4], "unit": 3, "pre": 3, "cycle": 22}

CALMING_BEGINNER = {"ratio": [1, 2, 1, 2], "unit": 3, "pre": 3, "cycle": 24}

CALMING_MEDIUM = {"ratio": [1, 3, 1, 3], "unit": 3, "pre": 3, "cycle": 22}

CALMING_ADVANCED = {"ratio": [1, 4, 1, 4], "unit": 3, "pre": 3, "cycle": 20}

CALMING2_BEGINNER = {"ratio": [5, 0, 5, 5], "unit": 1, "pre": 3, "cycle": 4}

CALMING2_MEDIUM = {"ratio": [5, 0, 5, 5], "unit": 1, "pre": 3, "cycle": 6}

CALMING2_ADVANCED = {"ratio": [5, 0, 5, 5], "unit": 1, "pre": 3, "cycle": 8}

POWER_BEGINNER = {"ratio": [1, 2, 2, 0], "unit": 3, "pre": 3, "cycle": 28}

POWER_MEDIUM = {"ratio": [1, 3, 2, 0], "unit": 3, "pre": 3, "cycle": 24}

POWER_ADVANCED = {"ratio": [1, 4, 2, 0], "unit": 3, "pre": 3, "cycle": 20}

HARMONY_BEGINNER = {"ratio": [1, 3, 2, 1], "unit": 3, "pre": 3, "cycle": 20}

HARMONY_MEDIUM = {"ratio": [1, 4, 2, 1], "unit": 3, "pre": 3, "cycle": 18}

HARMONY_ADVANCED = {"ratio": [1, 5, 2, 1], "unit": 3, "pre": 3, "cycle": 16}

RELAX2_BEGINNER = {
    "ratio": [
        4,
        7,
        8,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 4}

RELAX2_MEDIUM = {
    "ratio": [
        4,
        7,
        8,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 8}

RELAX2_ADVANCED = {
    "ratio": [
        4,
        7,
        8,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 12}

RELAX3_BEGINNER = {
    "ratio": [
        7,
        0,
        11,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 15}

RELAX3_MEDIUM = {
    "ratio": [
        7,
        0,
        11,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 20}

RELAX3_ADVANCED = {
    "ratio": [
        7,
        0,
        11,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 24}

ANTI_STRESS_BEGINNER = {
    "ratio": [
        3,
        0,
        0.66,
        0],
    "unit": 3,
    "pre": 3,
    "cycle": 20}

ANTI_STRESS_MEDIUM = {
    "ratio": [
        4,
        0,
        0.66,
        0],
    "unit": 3,
    "pre": 3,
    "cycle": 17}

ANTI_STRESS_ADVANCED = {
    "ratio": [
        5,
        0,
        0.66,
        0],
    "unit": 3,
    "pre": 3,
    "cycle": 14}

ANTI_APPETITE_BEGINNER = {
    "ratio": [
        5,
        0,
        5,
        5],
    "unit": 1,
    "pre": 3,
    "cycle": 40}

ANTI_APPETITE_MEDIUM = {
    "ratio": [
        6,
        0,
        5,
        5],
    "unit": 1,
    "pre": 3,
    "cycle": 38}

ANTI_APPETITE_ADVANCED = {
    "ratio": [
        7,
        0,
        5,
        5],
    "unit": 1,
    "pre": 3,
    "cycle": 36}

CIGARETTE_REPLACE_BEGINNER = {
    "ratio": [
        2,
        1.1,
        2.2,
        0.8],
    "unit": 2,
    "pre": 3,
    "cycle": 23}

CIGARETTE_REPLACE_MEDIUM = {
    "ratio": [
        3,
        1.1,
        2.2,
        0.8],
    "unit": 2,
    "pre": 3,
    "cycle": 21}

CIGARETTE_REPLACE_ADVANCED = {
    "ratio": [
        4,
        1.1,
        2.2,
        0.8],
    "unit": 2,
    "pre": 3,
    "cycle": 19}


DECISION_MAKING_BEGINNER = {
    "ratio": [
        5,
        2,
        7,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 6}

DECISION_MAKING_MEDIUM = {
    "ratio": [
        5,
        2,
        7,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 10}

DECISION_MAKING_ADVANCED = {
    "ratio": [
        5,
        2,
        7,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 14}

BALANCING_BEGINNER = {
    "ratio": [
        6,
        0,
        6,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 6}

BALANCING_MEDIUM = {
    "ratio": [
        8,
        1,
        8,
        1],
    "unit": 1,
    "pre": 3,
    "cycle": 8}

BALANCING_ADVANCED = {
    "ratio": [
        6,
        2,
        6,
        2],
    "unit": 1,
    "pre": 3,
    "cycle": 10}

ENERGIZING_BEGINNER = {
    "ratio": [
        6,
        0,
        4,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 6}

ENERGIZING_MEDIUM = {
    "ratio": [
        6,
        4,
        6,
        1],
    "unit": 1,
    "pre": 3,
    "cycle": 8}

ENERGIZING_ADVANCED = {
    "ratio": [
        6,
        6,
        6,
        1],
    "unit": 1,
    "pre": 3,
    "cycle": 10}


PROGRAMS = {"Clear Mind": {"Beginner": CLEAR_MIND_BEGINNER,
                           "Medium": CLEAR_MIND_MEDIUM,
                           "Advanced": CLEAR_MIND_ADVANCED},
            "Relax1": {"Beginner": RELAX_BEGINNER,
                       "Medium": RELAX_MEDIUM,
                       "Advanced": RELAX_ADVANCED},
            "Calming1": {"Beginner": CALMING_BEGINNER,
                         "Medium": CALMING_MEDIUM,
                         "Advanced": CALMING_ADVANCED},
            "Calming2": {"Beginner": CALMING2_BEGINNER,
                         "Medium": CALMING2_MEDIUM,
                         "Advanced": CALMING2_ADVANCED},
            "Power": {"Beginner": POWER_BEGINNER,
                      "Medium": POWER_MEDIUM,
                      "Advanced": POWER_ADVANCED},
            "Anti-Stress": {"Beginner": ANTI_STRESS_BEGINNER,
                            "Medium": ANTI_STRESS_MEDIUM,
                            "Advanced": ANTI_STRESS_ADVANCED},
            "Anti-Appetite": {"Beginner": ANTI_APPETITE_BEGINNER,
                              "Medium": ANTI_APPETITE_MEDIUM,
                              "Advanced": ANTI_APPETITE_ADVANCED},
            "Cigarette Replace": {"Beginner": CIGARETTE_REPLACE_BEGINNER,
                                  "Medium": CIGARETTE_REPLACE_MEDIUM,
                                  "Advanced": CIGARETTE_REPLACE_ADVANCED},
            "Harmony": {"Beginner": HARMONY_BEGINNER,
                        "Medium": HARMONY_MEDIUM,
                        "Advanced": HARMONY_ADVANCED},
            "Relax2": {"Beginner": RELAX2_BEGINNER,
                       "Medium": RELAX2_MEDIUM,
                       "Advanced": RELAX2_ADVANCED},
            "Relax3": {"Beginner": RELAX3_BEGINNER,
                       "Medium": RELAX3_MEDIUM,
                       "Advanced": RELAX3_ADVANCED},
            "Decision-Making": {"Beginner": DECISION_MAKING_BEGINNER,
                                "Medium": DECISION_MAKING_MEDIUM,
                                "Advanced": DECISION_MAKING_ADVANCED},
            "Balancing": {"Beginner": BALANCING_BEGINNER,
                          "Medium": BALANCING_MEDIUM,
                          "Advanced": BALANCING_ADVANCED},
            "Energizing": {"Beginner": ENERGIZING_BEGINNER,
                           "Medium": ENERGIZING_MEDIUM,
                           "Advanced": ENERGIZING_ADVANCED}
            }


SOUND_MAP = {
    "Silence": "silence.wav",
    "Start": "start.wav",
    "Prepare": "preparing.wav",
    "Inhale": "inhale.wav",
    "Exhale": "exhale.wav",
    "Retain": "retain.wav",
    "Sustain": "sustain.wav",
    "End": "well_done.wav",
}
