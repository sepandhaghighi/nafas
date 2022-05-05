# -*- coding: utf-8 -*-
"""
>>> from nafas.functions import *
>>> line(10,"*")
**********
>>> description_print()
Breathing  gymnastics  is  a  system of breathing exercises that focuses on the treatment of various
diseases  and  general  health  promotion. Nafas is a collection of breathing gymnastics designed to
reduce  the exhaustion of long working hours. With multiple breathing patterns, Nafas helps you find
your  way  to  a detoxified energetic workday and also improves your concentration by increasing the
oxygen  level.  No  need  to  walk away to take a break, just sit comfortably, run Nafas and let the
journey begin.
<BLANKLINE>
Please consider the following :
<BLANKLINE>
1. Inhaling is only done through the nose
2. Exhaling, you can use both nose and mouth
3. When exhaling through your mouth, it is recommended to fold the lips
<BLANKLINE>
>>> input_data = input_filter({"program":1,"level":1})
>>> input_data["program"] == 1
True
>>> input_data["level"] == 1
True
>>> input_data = input_filter({"program":20,"level":5})
>>> input_data["program"] == 1
True
>>> input_data["level"] == 1
True
>>> input_data = get_input_standard(lambda x: "1")
- Please choose a program :
<BLANKLINE>
1- Clear Mind (~ 7 minutes)
2- Relax1 (~ 7 minutes)
3- Relax2 (~ 3 minutes)
4- Relax3 (~ 6 minutes)
5- Calming (~ 9 minutes)
6- Power (~ 7 minutes)
7- Harmony (~ 7 minutes)
8- Anti-Stress (~ 4 minutes)
9- Anti-Appetite (~ 10 minutes)
10- Cigarette Replace (~ 5 minutes)
11- Decision-Making (~ 2 minutes)
- Please choose a level :
<BLANKLINE>
1- Beginner
2- Medium
3- Advanced
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
Cycle : 1 (Remaining : 1)
- Inhale for 1 sec
.
- Exhale for 3 sec
. . .
######################################################################
Cycle : 2 (Remaining : 0)
- Inhale for 1 sec
.
- Exhale for 3 sec
. . .
######################################################################
Well done!
>>> run({'cycle': 2, 'pre': 3, 'unit': 1, 'ratio': [1, 0, 3.3, 0]})
Preparing . . . 
######################################################################
Start
######################################################################
Cycle : 1 (Remaining : 1)
- Inhale for 1 sec
.
- Exhale for 3.3 sec
. . . .
######################################################################
Cycle : 2 (Remaining : 0)
- Inhale for 1 sec
.
- Exhale for 3.3 sec
. . . .
######################################################################
Well done!
>>> play_sound(1, debug=False).join()
>>> play_sound(1, debug=True).join()
ERROR : Unable to play sound.

"""
