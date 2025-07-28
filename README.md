<div align="center">
<img src="https://github.com/sepandhaghighi/nafas/raw/master/otherfiles/logo.png" width=320px>
<h1>Nafas: A Breathing Gymnastics Application</h1>
<hr>
<a href="https://badge.fury.io/py/nafas"><img src="https://badge.fury.io/py/nafas.svg" alt="PyPI version"></a>
<a href="https://codecov.io/gh/sepandhaghighi/nafas"><img src="https://codecov.io/gh/sepandhaghighi/nafas/branch/master/graph/badge.svg" alt="Codecov"></a>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
<a href="https://github.com/sepandhaghighi/nafas"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/sepandhaghighi/nafas"></a>
<a href="https://discord.gg/CtZUNKJHP4"><img src="https://img.shields.io/discord/901570530145107978.svg" alt="Discord Channel"></a>
</div>	

				
## Overview						
Breathing gymnastics is a system of breathing exercises that focuses on the treatment of various diseases and general health promotion.
**Nafas** is a collection of breathing gymnastics designed to reduce the exhaustion of long working hours.
With multiple breathing patterns, **Nafas** helps you find your way to a detoxified energetic workday and also improves your concentration by increasing the oxygen level.
No need to walk away to take a break, just sit comfortably, run **Nafas** and let the journey begin.
**Nafas** means breath in Persian.

**Nafas** offers a selection of predefined breathing exercise programs.
Each program consists of multiple cycles.
The exercises begin with a gentle preparation phase to help users settle in and focus, followed by a series of timed inhales and exhales.
Between these breaths, the programs incorporate deliberate pauses that allow users to retain and sustain their breath.
These cycles aim to enhance both physical and mental well-being.

<div align="center">
	<img src="https://github.com/sepandhaghighi/nafas/raw/master/otherfiles/overview.png" width=300px alt="Nafas Programs' Cycle">
	<p>Nafas Programs' Cycle</p>
</div>

<table>
	<tr> 
		<td align="center">Open Hub</td>
		<td align="center"><a href="https://www.openhub.net/p/nafas"><img src="https://www.openhub.net/p/nafas/widgets/project_thin_badge.gif"></a></td>	
	</tr>
	<tr>
		<td align="center">PyPI Counter</td>
		<td align="center"><a href="http://pepy.tech/project/nafas"><img src="http://pepy.tech/badge/nafas"></a></td>
	</tr>
	<tr>
		<td align="center">Github Stars</td>
		<td align="center"><a href="https://github.com/sepandhaghighi/nafas"><img src="https://img.shields.io/github/stars/sepandhaghighi/nafas.svg?style=social&label=Stars"></a></td>
	</tr>
</table>



<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">dev</td>	
	</tr>
	<tr>
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/sepandhaghighi/nafas/actions/workflows/test.yml/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/sepandhaghighi/nafas/actions/workflows/test.yml/badge.svg?branch=dev"></td>
	</tr>
</table>


<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://app.codacy.com/gh/sepandhaghighi/nafas/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/b2be5ce052bc43a89713ac4aec6f8d11"/></a></td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/sepandhaghighi/nafas"><img src="https://www.codefactor.io/repository/github/sepandhaghighi/nafas/badge" alt="CodeFactor" /></a></td>		
	</tr>
</table>


## Installation		

### Source Code
- Download [Version 1.4](https://github.com/sepandhaghighi/nafas/archive/v1.4.zip) or [Latest Source](https://github.com/sepandhaghighi/nafas/archive/dev.zip)
- `pip install .`				

### PyPI

- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- `pip install nafas==1.4`						
	

### Exe Version

⚠️ Only Windows

- Download [Exe-Version 1.4](https://github.com/sepandhaghighi/nafas/releases/download/v1.4/NAFAS-1.4.exe)
- Run `NAFAS-1.4.exe`


## Usage	

ℹ️ You can use `nafas`, `python -m nafas` or `NAFAS.exe` to run this program

ℹ️ Checkout the available programs in [PROGRAMS.md](https://github.com/sepandhaghighi/nafas/blob/master/PROGRAMS.md)

### Version

```console
nafas --version
```

### Basic

```console
nafas
```

### Silent Mode

ℹ️ This mode will disable the sound playing system

```console
nafas --silent
```	

### Speaker

ℹ️ Customize your experience by choosing from a set of speaker voices to guide you through the exercises.
You can specify the speaker using the `--speaker`:

```console
nafas --speaker=us1
```

Choose your speaker from the following list:
| ID | Description |
|:--:|:-----------:|
| `us1` | Feminine voice with a US accent |
| `us2` | Masculine voice with a US accent |
| `in1` | Feminine voice with an Indian accent |
| `in2` | Masculine voice with an Indian accent |
| `cn1` | Feminine voice with a Chinese accent |
| `cn2` | Masculine voice with a Chinese accent |
| `ca1` | Feminine voice with a Canadian accent |
| `ca2` | Masculine voice with a Canadian accent |
| `au1` | Feminine voice with an Australian accent |
| `au2` | Masculine voice with an Australian accent |
| `uk1` | Feminine voice with a British accent |
| `uk2` | Masculine voice with a British accent |


### Skip Intro

ℹ️ This mode will skip the introduction

```console
nafas --skip-intro
```	


### Custom Config

ℹ️ Users can load their custom configurations

```console
nafas --config="program1.json"
```

Config example:

```json
{
    "name": "program1",
    "unit": 2,
    "pre": 3,
    "cycle": 10,
    "ratio": {
        "inhale": 2,
        "exhale": 2,
        "retain": 3,
        "sustain": 4
    }
}
```

## Screen Record

<div align="center">

<img src="https://github.com/sepandhaghighi/nafas/raw/master/otherfiles/help.gif" alt="Screen Record">

</div>


## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!

- Please complete the issue template

You can also join our discord server

<a href="https://discord.gg/CtZUNKJHP4">
  <img src="https://img.shields.io/discord/901570530145107978.svg?style=for-the-badge" alt="Discord Channel">
</a>
 			

## References

<blockquote>1- <a href="https://pranabreath.info">Prana Breath</a> </blockquote>

<blockquote>2- Rickard, Kathleen Benjamin, Dorothy J. Dunn, and Virginia M. Brouch. "Breathing techniques associated with improved health outcomes." (2015). </blockquote>

<blockquote>3- Zaccaro, Andrea, Andrea Piarulli, Marco Laurino, Erika Garbella, Danilo Menicucci, Bruno Neri, and Angelo Gemignani. "How breath-control can change your life: a systematic review on psycho-physiological correlates of slow breathing." Frontiers in human neuroscience 12 (2018): 353. </blockquote>

<blockquote>4- Brook, Robert D., Lawrence J. Appel, Melvyn Rubenfire, Gbenga Ogedegbe, John D. Bisognano, William J. Elliott, Flavio D. Fuchs et al. "Beyond medications and diet: alternative approaches to lowering blood pressure: a scientific statement from the American Heart Association." Hypertension 61, no. 6 (2013): 1360-1383. </blockquote>	

<blockquote>5- Russo, Marc A., Danielle M. Santarelli, and Dean O’Rourke. "The physiological effects of slow breathing in the healthy human." Breathe 13, no. 4 (2017): 298-309. </blockquote>	

<blockquote>6- Bujatti, M., and P. Biederer. "Serotonin, noradrenaline, dopamine metabolites in transcendental meditation-technique." Journal of Neural Transmission 39, no. 3 (1976): 257-267. </blockquote>

<blockquote>7- Martarelli, Daniele, Mario Cocchioni, Stefania Scuri, and Pierluigi Pompei. "Diaphragmatic breathing reduces exercise-induced oxidative stress." Evidence-Based Complementary and Alternative Medicine 2011 (2011). </blockquote>		

<blockquote>8- <a href="https://www.drweil.com/videos-features/videos/breathing-exercises-4-7-8-breath/">DrWeil, Integrative Medicine & Healthy Living</a> </blockquote>

<blockquote>9- <a href="https://www.hgi.org.uk/resources/delve-our-extensive-library/resources-and-techniques/7-11-breathing-how-does-deep">Human Givens Institute</a> </blockquote>

<blockquote>10- <a href="https://www.inc.com/mithu-storoni/this-2-minute-breathing-exercise-can-help-you-make-better-decisions-according-to-a-new-study.html">This 2-Minute Breathing Exercise Can Help You Make Better Decisions</a> </blockquote>

<blockquote>11- <a href="https://k12.thoughtfullearning.com/minilesson/using-5-5-5-breathing-calm-down">Using 5-5-5 Breathing to Calm Down</a> </blockquote>
					
<blockquote>12- <a href="https://ttsmp3.com/">Free Text-To-Speech and Text-to-MP3 for US English</a> </blockquote>

<blockquote>13- <a href="https://www.yogabasics.com/practice/pranayama/">Pranayama Breathing Techniques and Tips</a> </blockquote>

<blockquote>14- <a href="https://health.clevelandclinic.org/box-breathing-benefits">Box Breathing Benefits and Techniques</a> </blockquote>

<blockquote>15- <a href="https://www.medicalnewstoday.com/articles/321805#how-to-do-it">Box breathing: How to do it, benefits, and tips</a> </blockquote>

<blockquote>16- <a href="https://pubmed.ncbi.nlm.nih.gov/24380741/">Breathing at a rate of 5.5 breaths per minute with equal inhalation-to-exhalation ratio increases heart rate variability</a> </blockquote>

<blockquote>17- <a href="https://www.youtube.com/watch?v=dPkpW5lqL3E">Coherent Breathing Timer - 6 Breaths Per Minute | 5 Seconds in / 5 Seconds Out | With Bells</a> </blockquote>

## Cite

If you use **Nafas** in your research, we would appreciate citations to the following paper:


[Sabouri, Sadra, and Sepand Haghighi. "Nafas: Breathing Gymnastics Application." *arXiv preprint arXiv:2412.04667* (2024).](https://arxiv.org/abs/2412.04667)


```bibtex
@article{sabouri2024nafas,
  title={Nafas: Breathing Gymnastics Application},
  author={Sabouri, Sadra and Haghighi, Sepand},
  journal={arXiv preprint arXiv:2412.04667},
  year={2024}
}
```

## Show Your Support
								
<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you!

<h3>Donate to Our Project</h3>	

<h4>Bitcoin</h4>
1KtNLEEeUbTEK9PdN6Ya3ZAKXaqoKUuxCy
<h4>Ethereum</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Litecoin</h4>
Ldnz5gMcEeV8BAdsyf8FstWDC6uyYR6pgZ
<h4>Doge</h4>
DDUnKpFQbBqLpFVZ9DfuVysBdr249HxVDh
<h4>Tron</h4>
TCZxzPZLcJHr2qR3uPUB1tXB6L3FDSSAx7
<h4>Ripple</h4>
rN7ZuRG7HDGHR5nof8nu5LrsbmSB61V1qq
<h4>Binance Coin</h4>
bnb1zglwcf0ac3d0s2f6ck5kgwvcru4tlctt4p5qef
<h4>Tether</h4>
0xcD4Db18B6664A9662123D4307B074aE968535388
<h4>Dash</h4>
Xd3Yn2qZJ7VE8nbKw2fS98aLxR5M6WUU3s
<h4>Stellar</h4>		
GALPOLPISRHIYHLQER2TLJRGUSZH52RYDK6C3HIU4PSMNAV65Q36EGNL
<h4>Zilliqa</h4>
zil1knmz8zj88cf0exr2ry7nav9elehxfcgqu3c5e5
<h4>Coffeete</h4>
<a href="http://www.coffeete.ir/opensource">
<img src="http://www.coffeete.ir/images/buttons/lemonchiffon.png" style="width:260px;" />
</a>
