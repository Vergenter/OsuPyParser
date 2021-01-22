[![PyPI version](https://badge.fury.io/py/OsuPyParser.svg)](https://badge.fury.io/py/OsuPyParser.svg)
# OsuPyParser 
A powerful package for parsing .osu extention file

## What's this?
OsuPyParser is simply parser for .osu files i made for my usage due i consistantly need it in my private repositories,
It can parse literally all major data from .osu file, even timing points.

## Example
Good packages need a good explanation how to use them so there it is!

```py
import osupyparser

osuMap = osupyparser.OsuParser("PATH TO A .osu FILE")

mapInfo = osuMap.parseMap()

print(mapInfo.formatVersion, mapInfo.artist)
```

## Contribution
If you feel like you want to help/fix/change something in this package,
just create Issue or Pull Request on GitHub and I'll review it.
