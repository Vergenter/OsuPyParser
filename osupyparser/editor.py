
class Editor:

    @classmethod
    def parse_header(cls, line: str, osu_map: object) -> None:

        if "DistanceSpacing" in line:
            osu_map.distance_spacing = float(line.split("DistanceSpacing: ")[1])
        if "BeatDivisor" in line:
            osu_map.beat_divisor = int(line.split("BeatDivisor: ")[1])
        if "GridSize" in line:
            osu_map.grid_size = int(line.split("GridSize: ")[1])
        if "TimelineZoom" in line:
            osu_map.timeline_zoom = float(line.split("TimelineZoom: ")[1])

