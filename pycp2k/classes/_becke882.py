from pycp2k.inputsection import InputSection


class _becke882(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self._name = "BECKE88"
        self._keywords = {'Scale_x': 'SCALE_X'}
        self._attributes = ['Section_parameters']

