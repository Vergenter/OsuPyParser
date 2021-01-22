
class Editor:

    def __init__(self):
        # easy instance to do
        self.distance_spacing: float = 0.0
        self.beat_divisor: int = 0
        self.grid_size: int = 0
        self.timeline_zoom: float = 0

    def parse(self, lines: str) -> None:

        if "DistanceSpacing" in lines:
            self.distance_spacing = float(lines.split("DistanceSpacing: ")[1])
        if "BeatDivisor" in lines:
            self.beat_divisor = int(lines.split("BeatDivisor: ")[1])
        if "GridSize" in lines:
            self.grid_size = int(lines.split("GridSize: ")[1])
        if "TimelineZoom" in lines:
            self.timeline_zoom = float(lines.split("TimelineZoom: ")[1])

editor = Editor()

