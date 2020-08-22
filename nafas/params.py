# -*- coding: utf-8 -*-
"""nafas parameters."""

STANDARD_MENU = {"program":{1:"Clear Mind",2:"Relax",3:"Calming",4:"Power",5:"Harmony",6:"Anti-Stress",7:"Anti-Appetite",8:"Cigarette Replace"},"level":{1:"Beginner",2:"Medium",3:"Advanced"}}

STEP_MAP = {0:"Inhale",1:"Retain",2:"Exhale",3:"Sustain"}

CLEAR_MIND_BEGINNER = {"ratio":[1,0,3,0],"unit":3,"pre":3,"cycle":35}

CLEAR_MIND_MEDIUM = {"ratio":[1,0,4,0],"unit":3,"pre":3,"cycle":28}

CLEAR_MIND_ADVANCED = {"ratio":[1,0,5,0],"unit":3,"pre":3,"cycle":24}

RELAX_BEGINNER = {"ratio":[1,0,2,2],"unit":3,"pre":3,"cycle":28}

RELAX_MEDIUM = {"ratio":[1,0,2,3],"unit":3,"pre":3,"cycle":24}

RELAX_ADVANCED = {"ratio":[1,0,2,4],"unit":3,"pre":3,"cycle":22}

CALMING_BEGINNER = {"ratio":[1,2,1,2],"unit":3,"pre":3,"cycle":24}

CALMING_MEDIUM = {"ratio":[1,3,1,3],"unit":3,"pre":3,"cycle":22}

CALMING_ADVANCED = {"ratio":[1,4,1,4],"unit":3,"pre":3,"cycle":20}

POWER_BEGINNER = {"ratio":[1,2,2,0],"unit":3,"pre":3,"cycle":28}

POWER_MEDIUM = {"ratio":[1,3,2,0],"unit":3,"pre":3,"cycle":24}

POWER_ADVANCED = {"ratio":[1,4,2,0],"unit":3,"pre":3,"cycle":20}


PROGRAMS = {"Clear Mind":{"Beginner":CLEAR_MIND_BEGINNER,"Medium":CLEAR_MIND_MEDIUM,"Advanced":CLEAR_MIND_ADVANCED},
            "Relax": {"Beginner":RELAX_BEGINNER,"Medium":RELAX_MEDIUM,"Advanced":RELAX_ADVANCED},
            "Calming" : {"Beginner":CALMING_BEGINNER,"Medium":CALMING_MEDIUM,"Advanced":CALMING_ADVANCED},
            "Power" : {"Beginner":POWER_BEGINNER,"Medium":POWER_MEDIUM,"Advanced":POWER_ADVANCED}

            }