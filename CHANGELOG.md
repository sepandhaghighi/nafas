# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.4] - 2025-07-29
### Added
- `ca1` speaker audio files
- `ca2` speaker audio files
- `au1` speaker audio files
- `au2` speaker audio files
- `uk1` speaker audio files
- `uk2` speaker audio files
### Changed
- Build script updated
- `README.md` modified
- `line` function renamed to `print_line`
- `bpm_calc` function renamed to `calculate_bpm`
- `time_calc` function renamed to `calculate_time`
- `time_average_calc` function renamed to `calculate_average_time`
- `time_convert` function renamed to `convert_time`
- `left_justify` function renamed to `justify_left`
- `justify` function renamed to `justify_text`
- `sound_check` function renamed to `check_sound`
- `nafas_description_print` function renamed to `print_nafas_description`
- `program_details_print` function renamed to `print_program_details`
- `input_filter` function renamed to `filter_input`
- `get_input_standard` function renamed to `get_standard_input`
- `run` function renamed to `run_program`
## [1.3] - 2025-06-27
### Added
- `--speaker` argument
- `us2` speaker audio files
- `in1` speaker audio files
- `in2` speaker audio files
- `cn1` speaker audio files
- `cn2` speaker audio files
### Changed
- `README.md` modified
## [1.2] - 2025-06-04
### Added
- Coherent program
- Breaths Per Minute (BPM)
### Changed
- `description_print` function renamed to `nafas_description_print`
- `program_description_print` function renamed to `program_details_print`
-  Python typing features added to all modules
-  `Python 3.6` support dropped
-  Test system modified
-  `PROGRAMS.md` updated
## [1.1] - 2025-04-10
### Added
- Survey form
- `--config` argument
- `--skip-intro` argument
### Changed
- `README.md` modified
## [1.0] - 2025-03-10
### Added
- Calming3 program
- Box program
### Changed
- `README.md` modified
- String templates modified
- `PROGRAMS.md` updated
## [0.9] - 2025-01-06
### Added
- Energizing program
- `PROGRAMS.md`
- Cautions message
### Changed
- `README.md` modified
- `AUTHORS.md` updated
- Menu updated
- Exit bug fixed
- Program details updated
## [0.8] - 2024-11-04
### Added
- Balancing program
- `--silent` argument
- `clear_screen` function
### Changed
- GitHub actions are limited to the `dev` and `master` branches
- Restart mode updated
- Exit bug fixed
- `Python 3.13` added to `test.yml`
- Messages and templates moved to `params.py`
## [0.7] - 2024-08-27
### Added
- `feature_request.yml` template
- `config.yml` for issue template
- `sound_check` function
- `SECURITY.md`
### Changed
- Silence added to the start of sounds
- Bug report template modified
- `playsound` replaced with `nava`
- `nava` added to `requirements.txt`
- Test system modified
- Build system modified
- `get_input_standard` function modified
- `Python 3.11` added to `test.yml`
- `Python 3.12` added to `test.yml`
- `Python 3.5` support dropped
- CLI mode updated
- Exit message updated
- `README.md` modified
## [0.6] - 2022-06-22
### Added
- Calming2 program
### Changed
- Calming program renamed to Calming1
- Logo updated
- `README.md` modified
## [0.5] - 2022-05-09
### Added
- Decision-Making program
- `time_calc` function
- `time_average_calc` function
### Changed
- `AUTHORS.md` updated
- License updated
- `README.md` modified
- `Python 3.10` added to `test.yml`
- `time_convert` function modified
- `get_input_standard` function modified
- Menu updated
- Relax program renamed to Relax1
- 4-7-8 program renamed to Relax2
- 7-11 program renamed to Relax3
## [0.4] - 2021-05-12
### Added
- `start.wav`
- `well_done.wav`
- `preparing.wav`
- `requirements-splitter.py`
- 4-7-8 program
- 7-11 program
### Changed
- Sound speaker changed
- Test system modified
- Menu optimized
## [0.3] - 2021-02-09
### Changed
- Sounds bug in pypi fixed
- Icon modified
- Menu optimized
## [0.2] - 2021-01-29
### Added
- `_playsound_async` function
- `play_sound` function
- `inhale.wav`
- `exhale.wav`
- `sustain.wav`
- `retain.wav`
- `get_sound_path` function
- `program_description_print` function
- `time_convert` function
### Changed
- Menu optimized
- Test system modified
- `get_program_dict` function renamed to `get_program_data`
- `program_dict` parameter renamed to `program_data`
- `input_dict` parameter renamed to `input_data`
- `README.md` updated
## [0.1] - 2020-10-30
### Added
- Clear Mind program
- Relax program
- Calming program
- Power program
- Anti-Stress program
- Anti-Appetite program 
- Cigarette Replace program

[Unreleased]: https://github.com/sepandhaghighi/nafas/compare/v1.4...dev
[1.4]: https://github.com/sepandhaghighi/nafas/compare/v1.3...v1.4
[1.3]: https://github.com/sepandhaghighi/nafas/compare/v1.2...v1.3
[1.2]: https://github.com/sepandhaghighi/nafas/compare/v1.1...v1.2
[1.1]: https://github.com/sepandhaghighi/nafas/compare/v1.0...v1.1
[1.0]: https://github.com/sepandhaghighi/nafas/compare/v0.9...v1.0
[0.9]: https://github.com/sepandhaghighi/nafas/compare/v0.8...v0.9
[0.8]: https://github.com/sepandhaghighi/nafas/compare/v0.7...v0.8
[0.7]: https://github.com/sepandhaghighi/nafas/compare/v0.6...v0.7
[0.6]: https://github.com/sepandhaghighi/nafas/compare/v0.5...v0.6
[0.5]: https://github.com/sepandhaghighi/nafas/compare/v0.4...v0.5
[0.4]: https://github.com/sepandhaghighi/nafas/compare/v0.3...v0.4
[0.3]: https://github.com/sepandhaghighi/nafas/compare/v0.2...v0.3
[0.2]: https://github.com/sepandhaghighi/nafas/compare/v0.1...v0.2
[0.1]: https://github.com/sepandhaghighi/nafas/compare/c58087a...v0.1



