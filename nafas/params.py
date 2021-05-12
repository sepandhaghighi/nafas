# -*- coding: utf-8 -*-
"""nafas parameters."""

NAFAS_DESCRIPTION = """
Breathing gymnastics is a system of breathing exercises that focuses on the treatment of various diseases and general health promotion.
Nafas is a collection of breathing gymnastics designed to reduce the exhaustion of long working hours.
With multiple breathing patterns, Nafas helps you find your way to a detoxified energetic workday and also improves your concentration by increasing the oxygen level.
No need to walk away to take a break, just sit comfortably, run Nafas and let the journey begin.
"""

NAFAS_NOTICE = """
Please consider the following :

1. Inhaling is only done through the nose
2. Exhaling, you can use both nose and mouth
3. When exhaling through your mouth, it is recommended to fold the lips
"""

NAFAS_VERSION = "0.4"

SOUND_ERROR_MESSAGE = "ERROR : Unable to play sound."

PROGRAM_DESCRIPTION = """Program Details :

Name             : {0}

Level            : {1}

Number of Cycles : {2}

Total Time       : {3}

Sequence         : {4}
"""

CYCLE_TEMPLATE = "Cycle : {0} (Remaining : {1})"

STEP_TEMPLATE = "- {0} for {1} sec"

STANDARD_MENU = {
    "program": {
        1: "Clear Mind",
        2: "Relax",
        3: "Calming",
        4: "Power",
        5: "Harmony",
        6: "Anti-Stress",
        7: "Anti-Appetite",
        8: "Cigarette Replace",
        9: "4-7-8(Relaxing Breath)",
        10: "7-11(Relaxing Breath)"},
    "level": {
        1: "Beginner",
        2: "Medium",
        3: "Advanced"}}

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

POWER_BEGINNER = {"ratio": [1, 2, 2, 0], "unit": 3, "pre": 3, "cycle": 28}

POWER_MEDIUM = {"ratio": [1, 3, 2, 0], "unit": 3, "pre": 3, "cycle": 24}

POWER_ADVANCED = {"ratio": [1, 4, 2, 0], "unit": 3, "pre": 3, "cycle": 20}

HARMONY_BEGINNER = {"ratio": [1, 3, 2, 1], "unit": 3, "pre": 3, "cycle": 20}

HARMONY_MEDIUM = {"ratio": [1, 4, 2, 1], "unit": 3, "pre": 3, "cycle": 18}

HARMONY_ADVANCED = {"ratio": [1, 5, 2, 1], "unit": 3, "pre": 3, "cycle": 16}

FOUR_SEVEN_EIGHT_BEGINNER = {
    "ratio": [
        4,
        7,
        8,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 4}

FOUR_SEVEN_EIGHT_MEDIUM = {
    "ratio": [
        4,
        7,
        8,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 8}

FOUR_SEVEN_EIGHT_ADVANCED = {
    "ratio": [
        4,
        7,
        8,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 12}

SEVEN_ELEVEN_BEGINNER = {
    "ratio": [
        7,
        0,
        11,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 15}

SEVEN_ELEVEN_MEDIUM = {
    "ratio": [
        7,
        0,
        11,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 20}

SEVEN_ELEVEN_ADVANCED = {
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


PROGRAMS = {"Clear Mind": {"Beginner": CLEAR_MIND_BEGINNER,
                           "Medium": CLEAR_MIND_MEDIUM,
                           "Advanced": CLEAR_MIND_ADVANCED},
            "Relax": {"Beginner": RELAX_BEGINNER,
                      "Medium": RELAX_MEDIUM,
                      "Advanced": RELAX_ADVANCED},
            "Calming": {"Beginner": CALMING_BEGINNER,
                        "Medium": CALMING_MEDIUM,
                        "Advanced": CALMING_ADVANCED},
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
            "4-7-8(Relaxing Breath)": {"Beginner": FOUR_SEVEN_EIGHT_BEGINNER,
                                       "Medium": FOUR_SEVEN_EIGHT_MEDIUM,
                                       "Advanced": FOUR_SEVEN_EIGHT_ADVANCED},
            "7-11(Relaxing Breath)": {"Beginner": SEVEN_ELEVEN_BEGINNER,
                                      "Medium": SEVEN_ELEVEN_MEDIUM,
                                      "Advanced": SEVEN_ELEVEN_ADVANCED}
            }


SOUND_MAP = {
    "Start": "start.wav",
    "Prepare": "preparing.wav",
    "Inhale": "inhale.wav",
    "Exhale": "exhale.wav",
    "Retain": "retain.wav",
    "Sustain": "sustain.wav",
    "End": "well_done.wav",
}
