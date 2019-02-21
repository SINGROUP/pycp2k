from pycp2k.inputsection import InputSection


class _ke_gga5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Functional = None
        self._name = "KE_GGA"
        self._keywords = {'Functional': 'FUNCTIONAL'}
        self._attributes = ['Section_parameters']

