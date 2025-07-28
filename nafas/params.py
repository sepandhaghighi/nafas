# -*- coding: utf-8 -*-
"""nafas parameters."""

NAFAS_VERSION = "1.4"

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

CONFIG_LOAD_ERROR_MESSAGE = "[Error] Failed to load the configuration file!"

PROGRAM_END_MESSAGE = "Well done!"

SURVEY_LINK_TEMPLATE = "https://opsclb.li/nafas/form?version={version}&data={data}"
SURVEY_DATA_TEMPLATE = "%7B\"name\":+\"{program_name}\",+\"level\":+\"{level}\",+\"data\":+%7B\"ratio\":+{ratio_rendered},+\"unit\":+{program_data_unit},+\"pre\":+{program_data_pre},+\"cycle\":+{program_data_cycle}%7D%7D"
SURVEY_MESSAGE_1 = "We are conducting a study to evaluate the usability of Nafas. By taking the following survey, you will contribute to our research and help us improve Nafas. The survey takes less than 5 minutes to complete.\n"
SURVEY_MESSAGE_2 = "Do you want to participate in the survey? (Y/[N])"

PROGRAM_DETAILS = """Program Details:

Name                     : {name}

Level                    : {level}

Number of Cycles         : {cycles}

Unit                     : {unit} seconds

Total Time               : {total_time}

Breaths per Minute (BPM) : {bpm}

Sequence                 : {sequence}
"""

MINUTES_TEMPLATE = "{minutes:02.0f} minutes"

SECONDS_TEMPLATE = "{seconds:02.0f} seconds"

PROGRAM_TIME_TEMPLATE = "{index}- {name} (~ {average_time})"

MENU_TEMPLATE_1 = "- Choose a {item}: \n"

MENU_TEMPLATE_2 = "{index}- {item}"

CYCLE_TEMPLATE = "Cycle: {cycle} (Remaining: {remaining})"

STEP_TEMPLATE = "- {step} for {time} seconds"

STANDARD_MENU = {
    "program": {
        1: "Clear Mind",
        2: "Relax1",
        3: "Relax2",
        4: "Relax3",
        5: "Calming1",
        6: "Calming2",
        7: "Calming3",
        8: "Power",
        9: "Harmony",
        10: "Anti-Stress",
        11: "Anti-Appetite",
        12: "Cigarette Replace",
        13: "Decision-Making",
        14: "Balancing",
        15: "Energizing",
        16: "Box",
        17: "Coherent"},
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

CALMING3_BEGINNER = {"ratio": [4, 0, 6, 0], "unit": 1, "pre": 3, "cycle": 6}

CALMING3_MEDIUM = {"ratio": [6, 1, 8, 4], "unit": 1, "pre": 3, "cycle": 8}

CALMING3_ADVANCED = {"ratio": [4, 1, 12, 1], "unit": 1, "pre": 3, "cycle": 10}

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


BOX_BEGINNER = {
    "ratio": [
        4,
        4,
        4,
        4],
    "unit": 1,
    "pre": 3,
    "cycle": 4}


BOX_MEDIUM = {
    "ratio": [
        4,
        4,
        4,
        4],
    "unit": 1,
    "pre": 3,
    "cycle": 8}


BOX_ADVANCED = {
    "ratio": [
        4,
        4,
        4,
        4],
    "unit": 1,
    "pre": 3,
    "cycle": 15}


COHERENT_BEGINNER = {
    "ratio": [
        5,
        0,
        5,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 30}


COHERENT_MEDIUM = {
    "ratio": [
        5,
        0,
        5,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 50}


COHERENT_ADVANCED = {
    "ratio": [
        5,
        0,
        5,
        0],
    "unit": 1,
    "pre": 3,
    "cycle": 70}


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
            "Calming3": {"Beginner": CALMING3_BEGINNER,
                         "Medium": CALMING3_MEDIUM,
                         "Advanced": CALMING3_ADVANCED},
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
                           "Advanced": ENERGIZING_ADVANCED},
            "Box": {"Beginner": BOX_BEGINNER,
                    "Medium": BOX_MEDIUM,
                    "Advanced": BOX_ADVANCED},
            "Coherent": {"Beginner": COHERENT_BEGINNER,
                         "Medium": COHERENT_MEDIUM,
                         "Advanced": COHERENT_ADVANCED},
            }

SPEAKER_LIST = [
    "us1", "us2",
    "in1", "in2",
    "cn1", "cn2",
    "ca1", "ca2",
    "au1", "au2",
    "uk1", "uk2",
]

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

CONFIG_VALIDATION_MAP = {
    "name": str,
    "ratio": {
        "inhale": (int, float),
        "exhale": (int, float),
        "retain": (int, float),
        "sustain": (int, float),
    },
    "unit": (int, float),
    "pre": (int, float),
    "cycle": int
}
