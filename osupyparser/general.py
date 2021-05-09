
class General:

    @classmethod
    def parse_header(cls, line: str, osu_map: object) -> None:
        # we will parse map strings
        not_parsed = True
        while not_parsed:
            if "AudioFilename" in line:
                osu_map.audio = str(line.split("AudioFilename: ")[1])
            elif "AudioLeadIn" in line:
                osu_map.lead_in = int(line.split("AudioLeadIn: ")[1])
            elif "PreviewTime" in line:
                osu_map.preview_time = int(line.split("PreviewTime: ")[1])
            elif "Countdown" in line:
                osu_map.countdown = int(line.split("Countdown: ")[1])
            elif "SampleSet" in line:
                osu_map.sample_set = str(line.split("SampleSet: ")[1])
            elif "StackLeniency" in line:
                osu_map.stack_leniency = float(line.split("StackLeniency: ")[1])
            elif "Mode" in line:
                osu_map.mode = int(line.split("Mode: ")[1])
            elif "LetterboxInBreaks" in line:
                osu_map.letterbox_in_breaks = int(line.split("LetterboxInBreaks: ")[1])
            elif "WidescreenStoryboard" in line:
                osu_map.widescreen_storyboard = int(line.split("WidescreenStoryboard: ")[1])
            not_parsed = False