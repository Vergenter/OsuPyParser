from .difficulty import Difficulty
from .editor import Editor
from .general import General
from .metadata import Metadata
from .timingpoints import TimingPoints
from .hitobject import HitObject
from .events import Events

class OsuFile:

    def __init__(self, file_path: str):
        """Initialise placeholders."""
        self._file_path: str = file_path

        # General.
        self.mode: int = 0
        self.file_version: int = 0
        self.audio: str = ""
        self.lead_in: int = 0
        self.preview_time: int = 0
        self.countdown: int = 0
        self.sample_set: str = ""
        self.stack_leniency: float = 0.0
        self.letterbox_in_breaks: int = 0
        self.widescreen_storyboard: int = 0

        # Editor.
        self.distance_spacing: float = 0.0
        self.grid_size: int = 0
        self.timeline_zoom: float = 0.0
        self.beat_divisor: int = 0
        self.time_start: int = 0
        self.time_end: int = 0
        self.play_length: float = 0.0
        self.drain_length: float = 0.0
        self.break_time: float = 0.0
        self.total_hits: float = 0.0

        # Difficulty.
        self.bpm: float = -1.00
        self.hp: float = 0.0
        self.cs: float = 0.0
        self.od: float = 0.0
        self.ar: float = 0.0
        self.slider_multiplier: float = 0.0
        self.slider_tick_rate: int = 0.0

        # Metadata.
        self.title: str = ""
        self.title_unicode: str = ""
        self.artist: str = ""
        self.artist_unicode: str = ""
        self.creator: str = ""
        self.version: str = ""
        self.tags: str = ""
        self.source: str = ""
        self.map_id: int = 0
        self.set_id: int = 0

        # TIMINGPOINTS AND HITOBJECTS
        self.timing_points: list = []
        self.hit_events: list = []

    def parse(self):
        """Function to get current section we are on and parse osu file data then return self."""

        # Open beatmap file.
        section_id = 0
        with open(self._file_path, "r") as stream:

            # First parse header from file.
            header_line = stream.readline()
            if "osu file format" not in header_line:
                raise ValueError("Unknown file header!")
            self.file_version = int(header_line[17:19])

            # Now parse section id.
            lines = stream.readlines()
            for one_line in lines:
                if not one_line or one_line == "":
                    # Skip empty line.
                    continue

                one_line = one_line.strip()

                if "[General]" in one_line:
                    # Set section id.
                    section_id = 1
                    continue
                elif "[Editor]" in one_line:
                    section_id = 2
                    continue
                elif "[Metadata]" in one_line:
                    section_id = 3
                    continue
                elif "[Difficulty]" in one_line:
                    section_id = 4
                    continue
                elif "[TimingPoints]" in one_line:
                    section_id = 5
                    continue
                elif "[HitObjects]" in one_line:
                    section_id = 6
                    continue
                elif "[Events]" in one_line:
                    section_id = 7
                    continue

                if section_id == 0:
                    continue

                func = {
                    1: General.parse_header,
                    2: Editor.parse_header,
                    3: Metadata.parse_header,
                    4: Difficulty.parse_header,
                    5: TimingPoints.parse_header,
                    6: HitObject.parse_header,
                    7: Events.parse_header
                }.get(section_id)
                func(one_line, self)

            # Parse some extra things.
            self.play_length = (self.time_end)/1000
            self.drain_length = max(0, (self.time_end - self.time_start - self.break_time) / 1000)
        return self

