from .difficulty import difficulty
from .editor import editor
from .general import general
from .metadata import metadata
from .timingpoints import timingpoint
from .hitobject import hitobject


class OsuParser:

    def __init__(self, filePath: str):
        self.filePath: str = filePath

        ### GENERAL ###
        self.mode: int = 0
        self.formatVersion: int = 0
        self.audio: str = ""
        self.leadIn: int = 0
        self.previewTime: int = 0
        self.countdown: int = 0
        self.sampleSet: str = ""
        self.stackLeniency: float = 0.0
        self.letterboxInBreaks: int = 0
        self.widescreenStoryboard: int = 0

        ### EDITOR ###
        self.distanceSpacing: float = 0.0
        self.gridSize: int = 0
        self.timelineZoom: float = 0.0
        self.beatDivisor: int = 0

        ### DIFFICULTY ###
        self.hp: int = 0
        self.cs: int = 0
        self.od: int = 0
        self.ar: int = 0
        self.sliderMultiplier: int = 0
        self.sliderTickRate: int = 0

        ### METADATA ###
        self.title: str = ""
        self.titleUnicode: str = ""
        self.artist: str = ""
        self.artistUnicode: str = ""
        self.creator: str = ""
        self.version: str = ""
        self.tags: str = ""
        self.source: str = ""
        self.mapID: int = 0
        self.setID: int = 0

        ### TIMINGPOINTS AND HITOBJECTS ###
        self.timingPoints = []
        self.hitEvents = []

    def parseMap(self):
        # parse map
        currentSection = ""
        file = open(self.filePath, 'rb')

        # small check
        if "osu file format" not in (formatVersion := file.readline().strip().decode("utf-8")):
            raise ValueError('Unknown header')
        else:
            self.formatVersion = int(formatVersion[17:19])

        while True:

            # loop it
            line = file.readline()

            if not line:
                break

            header = line.strip().decode("utf-8")

            # line is empty
            if header == "":
                continue

            ### SECTIONS ###
            if header == "[General]":
                currentSection = "General"
                continue
            if header == "[Editor]":
                currentSection = "Editor"
                continue
            if header == "[Metadata]":
                currentSection = "Metadata"
                continue
            if header == "[Difficulty]":
                currentSection = "Difficulty"
                continue
            if header == "[TimingPoints]":
                currentSection = "TimingPoints"
                continue
            if header == "[HitObjects]":
                currentSection = "HitObjects"
                continue

            ### SECTIONS PARSER ###
            if currentSection == "General":
                general.parse(header)
                ### fill the self with parsed ###
                self.mode = general.mode
                self.audio = general.audio_name
                self.leadIn = general.audio_lead_in
                self.previewTime = general.preview_time
                self.countdown = general.count_down
                self.sampleSet = general.sample_set
                self.stackLeniency = general.stack_leniency
                self.letterboxInBreaks = general.letterbox_in_breaks
                self.widescreenStoryboard = general.widescreen_storyboard
            if currentSection == "Editor":
                editor.parse(header)
                self.distanceSpacing = editor.distance_spacing
                self.gridSize = editor.grid_size
                self.timelineZoom = editor.timeline_zoom
                self.beatDivisor = editor.beat_divisor
            if currentSection == "Metadata":
                metadata.parse(header)
                self.title = metadata.title
                self.titleUnicode = metadata.title_unicode
                self.artist =  metadata.artist
                self.artistUnicode = metadata.artist_unicode
                self.creator = metadata.creator
                self.version = metadata.version
                self.tags = metadata.tags
                self.source = metadata.source
                self.mapID = metadata.beatmap_id
                self.setID = metadata.beatmapset_id
            if currentSection == "Difficulty":
                difficulty.parse(header)
                self.hp = difficulty.hp
                self.cs = difficulty.cs
                self.od = difficulty.od
                self.ar = difficulty.ar
                self.sliderMultiplier = difficulty.slider_multiplier
                self.sliderTickRate = difficulty.slider_tick_rate
            if currentSection == "TimingPoints":
                timingpoint.parse(header)
                self.timingPoints = timingpoint.timing_points
            if currentSection == "HitObjects":
                hitobject.parse(header)
                self.hitEvents = hitobject.hit_object
        file.close()
        return self
