from .timingpoint import TimingPoint

class TimingPoints:
    def __init__(self):
        self.timing_points = []

    def parse(self, lines: str) -> None:
        line = lines.split(',')
        # try method on stupid [coLoURs]
        try:
            time = int(line[0])
            beat_length = float(line[1])
            bpm = int(line[2])
            sample_set = int(line[3])
            sample_index = int(line[4])
            sample_vol = int(line[5])
            uninherited = int(line[6]) == 1
            effects = int(line[7])

            self.timing_points.append(TimingPoint(time, beat_length, bpm, sample_set, sample_index, sample_vol, uninherited, effects))
        except ValueError:
            # we got an stupid [Colours]
            # just skip it
            pass

timingpoint = TimingPoints()