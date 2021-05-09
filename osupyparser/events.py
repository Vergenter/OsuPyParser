
class Events:

    @classmethod
    def parse_header(cls, line: str, osu_map: object):

        if line == "\n" or line == "":
            return
        if not line.startswith("//"):
            item = line.split(",")
            if int(item[0]) == 2:
                osu_map.break_time += int(item[2]) - int(item[1])
