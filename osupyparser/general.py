### I DONT FEEL LIKE MAKING THIS ASYNC AT ALL CUZ IT MIGTH BREAK PERFORMANCE ###

class General:

    # we making intance of class
    def __init__(self):
        self.audio_name: str = ""
        self.audio_lead_in: int = 0
        self.preview_time: int = 0
        self.count_down: int = 0
        self.sample_set: str = ""
        self.stack_leniency: float = 0.0
        self.mode: int = 0
        self.letterbox_in_breaks: int = 0
        self.widescreen_storyboard: int = 0

    def parse(self, lines: str) -> None:
        # we will parse map strings
        if "AudioFilename" in lines:
            # we will use split()[1] to get info
            self.audio_name = str(lines.split("AudioFilename: ")[1])
        if "AudioLeadIn" in lines:
            self.audio_lead_in = int(lines.split("AudioLeadIn: ")[1])
        if "PreviewTime" in lines:
            self.preview_time = int(lines.split("PreviewTime: ")[1])
        if "Countdown" in lines:
            self.count_down = int(lines.split("Countdown: ")[1])
        if "SampleSet" in lines:
            self.sample_set = str(lines.split("SampleSet: ")[1])
        if "StackLeniency" in lines:
            self.stack_leniency = float(lines.split("StackLeniency: ")[1])
        if "Mode" in lines:
            self.mode = int(lines.split("Mode: ")[1])
        if "LetterboxInBreaks" in lines:
            self.letterbox_in_breaks = int(lines.split("LetterboxInBreaks: ")[1])
        if "WidescreenStoryboard" in lines:
            self.widescreen_storyboard = int(lines.split("WidescreenStoryboard: ")[1])

general = General()
