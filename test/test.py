# -*- coding: utf-8 -*-
"""
>>> from nafas.functions import *
>>> line(10,"*")
**********
>>> description_print()
 _   _          __
| \ | |  __ _  / _|  __ _  ___
|  \| | / _` || |_  / _` |/ __|
| |\  || (_| ||  _|| (_| |\__ \
|_| \_| \__,_||_|   \__,_||___/


         ___      _
__   __ / _ \    / |
\ \ / /| | | |   | |
 \ V / | |_| | _ | |
  \_/   \___/ (_)|_|


Breathing  gymnastics  is a system of breathing exercises that focuses
on  the  treatment  of  various diseases and general health promotion.
Breathing  gymnastics  is  an  excellent  means of coping with stress,
insomnia, fatigue, loss of strength, and even obesity.


>>> input_filter({"program":1,"level":1})
{'program': 1, 'level': 1}
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
"""
