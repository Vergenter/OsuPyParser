
class Metadata:

    def __init__(self):
        self.title: str = ""
        self.title_unicode: str = ""
        self.artist: str = ""
        self.artist_unicode: str = ""
        self.creator: str = ""
        self.version: str = ""
        self.source: str = ""
        self.tags: str = ""
        self.beatmap_id: int = 0
        self.beatmapset_id: int = 0

    def parse(self, lines: str) -> None:

        if "Title:" in lines:
            self.title = str(lines.split("Title:")[1])
        if "TitleUnicode" in lines:
            self.title_unicode = str(lines.split("TitleUnicode:")[1])
        if "Artist:" in lines:
            self.artist = str(lines.split("Artist:")[1])
        if "ArtistUnicode" in lines:
            self.artist_unicode = str(lines.split("ArtistUnicode:")[1])
        if "Creator" in lines:
            self.creator = str(lines.split("Creator:")[1])
        if "Version" in lines:
            self.version = str(lines.split("Version:")[1])
        if "Source" in lines:
            self.source = str(lines.split("Source:")[1])
        if "Tags" in lines:
            self.tags = str(lines.split("Tags:")[1])
        if "BeatmapID:" in lines:
            self.beatmap_id = int(lines.split("BeatmapID:")[1])
        if "BeatmapSetID" in lines:
            self.beatmapset_id = int(lines.split("BeatmapSetID:")[1])

metadata = Metadata()
