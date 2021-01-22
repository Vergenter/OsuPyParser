class HitObjects(object):
    def __init__(self, x, y, time, params):
        self.x = x
        self.y = y
        self.time = time
        self.params = params

class HitCircle(HitObjects):
    def __init__(self, x, y, time, params):
        super().__init__(x, y, time, params)

class Slider(HitObjects):
    def __init__(self, x, y, time, params):
        super().__init__(x, y, time, params)

class Spinner(HitObjects):
    def __init__(self, x, y, time, params):
        super().__init__(x, y, time, params)

class ManiaHold(HitObjects):
    def __init__(self, x, y, time, params):
        super().__init__(x, y, time, params)

