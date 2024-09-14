# -*- coding: utf-8 -*-
"""
>>> import os
>>> import doctest
>>> doctest.ELLIPSIS_MARKER = "ignore_this_message"
>>> from pytest import warns
>>> import shutil
>>> from nafas.functions import *
>>> clear_screen()

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
>>> print("\\n".join(justify(["123"], 2)))
123
>>> print("\\n".join(justify(["123"], 1)))
123
>>> print("\\n".join(justify(["123"], 0)))
123
>>> print("\\n".join(justify("", 2)))
<BLANKLINE>
>>> print("\\n".join(justify([" 1", "2", "3"], 2)))
1
2
3
>>> print("\\n".join(justify([" 1", "2", "3"], 3)))
1
2
3
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
5- Calming1 (~ 9 minutes)
6- Calming2 (~ 2 minutes)
7- Power (~ 7 minutes)
8- Harmony (~ 7 minutes)
9- Anti-Stress (~ 4 minutes)
10- Anti-Appetite (~ 10 minutes)
11- Cigarette Replace (~ 5 minutes)
12- Decision-Making (~ 2 minutes)
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
>>> run({'cycle': 2, 'pre': 3, 'unit': 1, 'ratio': [1, 0, 3, 0]}, silent=True)
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
>>> sid = play_sound(1)
Traceback (most recent call last):
        ...
nava.errors.NavaBaseError: Sound file's path should be a string.
>>> try:
...     wave_path = os.path.join("nafas", "sounds", "silence.wav")
...     temp_path = os.path.join("nafas", "sounds", "temp.wav")
...     _ = shutil.move(wave_path, temp_path)
...     with warns(RuntimeWarning, match="Your device is not compatible with our underlying sound-playing library. You can refer to https://github.com/openscilab/nava."):
...         sound_check_flag = sound_check()
...     _ = shutil.move(temp_path, wave_path)
... except Exception:
...     pass
>>> sound_check_flag
False
"""
