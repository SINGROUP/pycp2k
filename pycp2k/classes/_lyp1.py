from pycp2k.inputsection import InputSection


class _lyp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_c = None
        self._name = "LYP"
        self._keywords = {'Scale_c': 'SCALE_C'}
        self._attributes = ['Section_parameters']

