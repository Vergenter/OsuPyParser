from osupyparser import OsuFile

osuMap = OsuFile("./test.osu")

mapInfo = osuMap.parse()

print(f"{mapInfo.bpm}bpm {mapInfo.artist}")
