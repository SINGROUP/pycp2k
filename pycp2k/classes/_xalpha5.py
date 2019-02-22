from pycp2k.inputsection import InputSection


class _xalpha5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Xa = None
        self.Scale_x = None
        self._name = "XALPHA"
        self._keywords = {'Xa': 'XA', 'Scale_x': 'SCALE_X'}
        self._attributes = ['Section_parameters']

