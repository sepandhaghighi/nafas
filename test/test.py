# -*- coding: utf-8 -*-
"""
>>> from nafas.functions import *
>>> line(10,"*")
**********
>>> description_print()
Breathing  gymnastics  is a system of breathing exercises that focuses
on  the  treatment  of  various diseases and general health promotion.
Nafas  is  a collection of breathing gymnastics designed to reduce the
exhaustion  of  long  working hours. With multiple breathing patterns,
Nafas  helps  you  find your way to a detoxified energetic workday and
also  improves  your  concentration by increasing the oxygen level. No
need to walk away to take a break, just sit comfortably, run Nafas and
let the journey begin.
<BLANKLINE>
<BLANKLINE>
>>> input_data = input_filter({"program":1,"level":1})
>>> input_data["program"] == 1
True
>>> input_data["level"] == 1
True
>>> input_data = input_filter({"program":10,"level":5})
>>> input_data["program"] == 1
True
>>> input_data["level"] == 1
True
>>> input_data = get_input_standard(lambda x: "1")
- Please choose a level :
1- Beginner
2- Medium
3- Advanced
- Please choose a program :
1- Clear Mind
2- Relax
3- Calming
4- Power
5- Harmony
6- Anti-Stress
7- Anti-Appetite
8- Cigarette Replace
>>> input_data["program"] == 1
True
>>> input_data["level"] == 1
True
>>> program_name,level,program_data = get_program_data({"program":1,"level":1})
>>> program_data["pre"] == 3
True
>>> program_data["unit"] == 3
True
>>> program_description_print("Clear Mind","Beginner",{"ratio": [1, 0, 3, 0], "unit": 3, "pre": 3, "cycle": 35})
######################################################################
Program Details :
<BLANKLINE>
Name             : Clear Mind
<BLANKLINE>
Level            : Beginner
<BLANKLINE>
Number of Cycles : 35
<BLANKLINE>
Total Time       : 07 minutes, 03 seconds
<BLANKLINE>
Sequence         : Inhale, Exhale
<BLANKLINE>
######################################################################
>>> run({'cycle': 2, 'pre': 3, 'unit': 1, 'ratio': [1, 0, 3, 0]})
Preparing . . .
######################################################################
Start
######################################################################
Cycle : 1
- Inhale for 1 sec
.
- Exhale for 3 sec
. . .
######################################################################
Cycle : 2
- Inhale for 1 sec
.
- Exhale for 3 sec
. . .
######################################################################
End!
>>> run({'cycle': 2, 'pre': 3, 'unit': 1, 'ratio': [1, 0, 3.3, 0]})
Preparing . . . 
######################################################################
Start
######################################################################
Cycle : 1
- Inhale for 1 sec
.
- Exhale for 3.3 sec
. . . .
######################################################################
Cycle : 2
- Inhale for 1 sec
.
- Exhale for 3.3 sec
. . . .
######################################################################
End!
>>> play_sound(1, debug=False).join()
>>> play_sound(1, debug=True).join()
ERROR : Unable to play sound.

"""
