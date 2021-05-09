
class Metadata:

    @classmethod
    def parse_header(cls, line: str, osu_map: object) -> None:

        if "Title:" in line:
            osu_map.title = str(line.split("Title:")[1])
        if "TitleUnicode" in line:
            osu_map.title_unicode = str(line.split("TitleUnicode:")[1])
        if "Artist:" in line:
            osu_map.artist = str(line.split("Artist:")[1])
        if "ArtistUnicode" in line:
            osu_map.artist_unicode = str(line.split("ArtistUnicode:")[1])
        if "Creator" in line:
            osu_map.creator = str(line.split("Creator:")[1])
        if "Version" in line:
            osu_map.version = str(line.split("Version:")[1])
        if "Source" in line:
            osu_map.source = str(line.split("Source:")[1])
        if "Tags" in line:
            osu_map.tags = str(line.split("Tags:")[1])
        if "BeatmapID:" in line:
            osu_map.map_id = int(line.split("BeatmapID:")[1])
        if "BeatmapSetID" in line:
            osu_map.set_id = int(line.split("BeatmapSetID:")[1])

