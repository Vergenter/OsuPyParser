from .const import OBJECT_TYPE
from .hitobjects import Slider, Spinner, ManiaHold, HitObjects, HitCircle, ComboSkip

# Define it to cache.
SLIDER_TYPES = ['C','L','P','B']

class HitObject:

    @classmethod
    def parse_header(cls, line: str, osu_map: object):

        item = line.split(",")
        if not osu_map.hit_events: first_line = True
        else: first_line = False
        x = int(item[0])
        y = int(item[1])
        time = int(item[2])
        hit_type = int(item[3])
        hitsound = int(item[4])
        params = None
        info = dict()
        if first_line:
            osu_map.time_start = time
        else:
            osu_map.time_end = time

        if len(item) > 5:
            # Check for external params.
            if not any(curve_type == item[5][0] for curve_type in SLIDER_TYPES):
                params = line[5]
            else:
                try:
                    slider_info = item[5].split("|")
                    info['curve_type'] = slider_info[0]
                    info['curve_points'] = object(slider_info[1].split(":"))
                    info['slides'] = item[6]
                    info['length'] = item[7]
                    info['edge_sounds'] = item[8]
                    info['edge_sets'] = item[9]
                except Exception:
                    pass

        target_object = HitObjects

        if hit_type & OBJECT_TYPE.HIT_CIRCLE: target_object = HitCircle
        elif hit_type & OBJECT_TYPE.SLIDER: target_object = Slider
        elif hit_type & OBJECT_TYPE.COMBO_SKIP: target_object = ComboSkip
        elif hit_type & OBJECT_TYPE.SPINNER: target_object = Spinner
        elif hit_type & OBJECT_TYPE.MANIAHOLD: target_object = ManiaHold

        if not info:
            osu_map.hit_events.append(target_object(x, y, time, hitsound, params))
        else:
            osu_map.hit_events.append(target_object(x, y, time, hitsound, params, **info))
