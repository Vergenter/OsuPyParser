class TimingPoint:
  def __init__(self, time = 0, beatLength = 0, beatsPerMeasure = 0, sampleSet = 0, sampleIdx = 0, sampleVol = 0, uninherited = False, effects = 0):
    self.time = time
    self.beatLength = beatLength
    self.beatsPerMeasure = beatsPerMeasure
    self.sampleSet = sampleSet
    self.sampleIdx = sampleIdx
    self.sampleVol = sampleVol
    self.uninherited = uninherited
    self.effects = effects