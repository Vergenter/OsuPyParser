
class Difficulty:
    
    @classmethod
    def parse_header(cls, line: str, osu_map: object):

        if "HPDrainRate" in line:
            osu_map.hp = float(line.split("HPDrainRate:")[1])
        if "CircleSize" in line:
            osu_map.cs = float(line.split("CircleSize:")[1])
        if "OverallDifficulty" in line:
            osu_map.od = float(line.split("OverallDifficulty:")[1])
        if "ApproachRate" in line:
            osu_map.ar = float(line.split("ApproachRate:")[1])
        if "SliderMultiplier" in line:
            osu_map.slider_multiplier = float(line.split("SliderMultiplier:")[1])
        if "SliderTickRate" in line:
            osu_map.slider_tick_rate = int(line.split("SliderTickRate:")[1])
