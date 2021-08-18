from .timingpoint import TimingPoint

class TimingPoints:

    @classmethod
    def parse_header(cls, line: str, osu_map: object) -> None:

        item = line.split(',')
        if not osu_map.timing_points: first_line = True
        else: first_line = False

        # try method on stupid [coLoURs]
        try:
            if first_line:
                osu_map.bpm = round(1000/float(item[1])*60, 2)
            time = int(item[0])
            beat_length = float(item[1])
            bpm = int(item[2])
            sample_set = int(item[3])
            sample_index = int(item[4])
            sample_vol = int(item[5])
            uninherited = int(item[6]) == 1
            effects = int(item[7])

            osu_map.timing_points.append(TimingPoint(time, beat_length, bpm, sample_set, sample_index, sample_vol, uninherited, effects))
        except ValueError:
            # we got an stupid [Colours]
            # just skip it
            pass