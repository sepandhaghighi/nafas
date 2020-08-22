# -*- coding: utf-8 -*-
"""nafas parameters."""

STANDARD_MENU = {"program":{1:"Clear Mind",2:"Relax",3:"Calming",4:"Power",5:"Harmony",6:"Anti-Stress",7:"Anti-Appetite",8:"Cigarette Replace"},"level":{1:"Beginner",2:"Medium",3:"Advanced"}}

STEP_MAP = {0:"Inhale",1:"Retain",2:"Exhale",3:"Sustain"}

CLEAR_MIND_BEGINNER = {"ratio":[1,0,3,0],"unit":3,"pre":3,"cycle":35}

CLEAR_MIND_MEDIUM = {"ratio":[1,0,4,0],"unit":3,"pre":3,"cycle":28}

CLEAR_MIND_ADVANCED = {"ratio":[1,0,5,0],"unit":3,"pre":3,"cycle":24}

PROGRAMS = {"Clear Mind":{"Beginner":CLEAR_MIND_BEGINNER,"Medium":CLEAR_MIND_MEDIUM,"Advanced":CLEAR_MIND_ADVANCED}