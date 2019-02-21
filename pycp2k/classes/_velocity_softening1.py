from pycp2k.inputsection import InputSection


class _velocity_softening1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Steps = None
        self.Delta = None
        self.Alpha = None
        self._name = "VELOCITY_SOFTENING"
        self._keywords = {'Delta': 'DELTA', 'Steps': 'STEPS', 'Alpha': 'ALPHA'}

