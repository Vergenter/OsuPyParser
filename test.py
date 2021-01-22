import osupyparser

osuMap = osupyparser.OsuParser("PATH TO A .osu FILE")

mapInfo = osuMap.parseMap()

print(mapInfo.formatVersion, mapInfo.artist)