# -*- coding: utf-8 -*-
"""
Custom configurations must reject invalid numeric values before a program starts.

>>> from copy import deepcopy
>>> import json
>>> import os
>>> import tempfile
>>> from nafas.functions import load_config, validate_config
>>> from nafas.params import CONFIG_EXAMPLE
>>> invalid_configs = []
>>> for key in ("cycle", "unit", "pre"):
...     config = deepcopy(CONFIG_EXAMPLE)
...     config[key] = -1
...     invalid_configs.append(config)
>>> for key in ("inhale", "retain", "exhale", "sustain"):
...     config = deepcopy(CONFIG_EXAMPLE)
...     config["ratio"][key] = -0.5
...     invalid_configs.append(config)
>>> [validate_config(config) for config in invalid_configs]
[False, False, False, False, False, False, False]

A breathing cycle needs a positive total duration to calculate its BPM.

>>> config = deepcopy(CONFIG_EXAMPLE)
>>> config["unit"] = 0
>>> invalid_configs.append(config)
>>> validate_config(config)
False
>>> config = deepcopy(CONFIG_EXAMPLE)
>>> config["ratio"] = dict.fromkeys(config["ratio"], 0)
>>> invalid_configs.append(config)
>>> validate_config(config)
False

Invalid files should use the existing load-error result.

>>> results = []
>>> with tempfile.TemporaryDirectory() as directory:
...     path = os.path.join(directory, "config.json")
...     for config in invalid_configs:
...         with open(path, "w") as config_file:
...             json.dump(config, config_file)
...         results.append(load_config(path)["status"])
>>> results
[False, False, False, False, False, False, False, False, False]

Zero preparation time and skipped breathing phases remain valid, as do fractional durations.

>>> config = deepcopy(CONFIG_EXAMPLE)
>>> config.update(unit=0.5, pre=0, cycle=0)
>>> config["ratio"].update(retain=0, sustain=0, inhale=0.5)
>>> validate_config(config)
True
>>> config["cycle"] = 1.5
>>> validate_config(config)
False
>>> config["cycle"] = 1
>>> config["unit"] = "1"
>>> validate_config(config)
False
"""
