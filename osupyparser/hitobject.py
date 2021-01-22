from .const import OBJECT_TYPE
from .hitobjects import Slider, Spinner, ManiaHold, HitObjects, HitCircle

class HitObject:
    def __init__(self):
        self.hit_object = []

    def parse(self, lines: str):

        line = lines.split(",")
        x = int(line[0])
        y = int(line[1])
        time = int(line[2])
        hit_type = int(line[3])
        params = line[5]

        target_object = HitObjects

        if hit_type & OBJECT_TYPE.HIT_CIRCLE or hit_type & OBJECT_TYPE.HIT_CIRCLE_NEW: target_object = HitCircle
        elif hit_type & OBJECT_TYPE.SLIDER: target_object = Slider
        elif hit_type & OBJECT_TYPE.SPINNER: target_object = Spinner
        elif hit_type & OBJECT_TYPE.MANIAHOLD: target_object = ManiaHold

        self.hit_object.append(target_object(x, y, time, params))

hitobject = HitObject()

