class HitObjects(object):
    def __init__(self, x, y, time, hitsound, params = None, **kwargs):
        self.x = x
        self.y = y
        self.time = time
        self.hitsound = hitsound
        self.params = params
        self.curve_type = kwargs.get("curve_type", None)
        self.curve_points = kwargs.get("curve_points", None)
        self.slides = kwargs.get("slides", None)
        self.length = kwargs.get("length", None)
        self.edge_sounds = kwargs.get("edge_sounds", None)
        self.edge_sets = kwargs.get("edge_sets", None)

class HitCircle(HitObjects):
    def __init__(self, x, y, time, hitsound, params = None, **kwargs):
        super().__init__(x, y, time, hitsound, params, **kwargs)

class Slider(HitObjects):
    def __init__(self, x, y, time, hitsound, params = None, **kwargs):
        super().__init__(x, y, time, hitsound, params, **kwargs)

class ComboSkip(HitObjects):
    def __init__(self, x, y, time, hitsound, params = None, **kwargs):
        super().__init__(x, y, time, hitsound, params, **kwargs)

class Spinner(HitObjects):
    def __init__(self, x, y, time, hitsound, params = None, **kwargs):
        super().__init__(x, y, time, hitsound, params, **kwargs)

class ManiaHold(HitObjects):
    def __init__(self, x, y, time, hitsound, params = None, **kwargs):
        super().__init__(x, y, time, hitsound, params, **kwargs)

