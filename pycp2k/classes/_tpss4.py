from pycp2k.inputsection import InputSection


class _tpss4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Scale_c = None
        self._name = "TPSS"
        self._keywords = {'Scale_x': 'SCALE_X', 'Scale_c': 'SCALE_C'}
        self._attributes = ['Section_parameters']

