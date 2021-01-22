
class Difficulty:

    def __init__(self):
        self.hp: float = 0.0
        self.cs: float = 0.0
        self.od: float = 0.0
        self.ar: float = 0.0
        self.slider_multiplier: int = 0
        self.slider_tick_rate: int = 0

    def parse(self, lines: str):

        if "HPDrainRate" in lines:
            self.hp = float(lines.split("HPDrainRate:")[1])
        if "CircleSize" in lines:
            self.cs = float(lines.split("CircleSize:")[1])
        if "OverallDifficulty" in lines:
            self.od = float(lines.split("OverallDifficulty:")[1])
        if "ApproachRate" in lines:
            self.ar = float(lines.split("ApproachRate:")[1])
        if "SliderMultiplier" in lines:
            self.slider_multiplier = int(lines.split("SliderMultiplier:")[1])
        if "SliderTickRate" in lines:
            self.slider_tick_rate = int(lines.split("SliderTickRate:")[1])
            
difficulty = Difficulty()