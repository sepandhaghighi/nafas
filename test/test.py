# -*- coding: utf-8 -*-
"""
>>> from nafas.functions import *
>>> line(10,"*")
**********
>>> description_print()
Breathing  gymnastics  is a system of breathing exercises that focuses
on  the  treatment  of  various diseases and general health promotion.
Breathing  gymnastics  is  an  excellent  means of coping with stress,
insomnia, fatigue, loss of strength, and even obesity.
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
>>> program_data = get_program_dict({"program":1,"level":1})
>>> program_data["pre"] == 3
True
>>> program_data["unit"] == 3
True
>>> run({'cycle': 2, 'pre': 3, 'unit': 1, 'ratio': [1, 0, 3, 0]})
Preparing . . .
1
2
3
######################################################################
Start
######################################################################
Cycle : 1
- Inhale for 1 sec
- Exhale for 3 sec
######################################################################
Cycle : 2
- Inhale for 1 sec
- Exhale for 3 sec
######################################################################
End!

"""
