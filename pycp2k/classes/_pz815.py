from pycp2k.inputsection import InputSection


class _pz815(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Parametrization = None
        self.Scale_c = None
        self._name = "PZ81"
        self._keywords = {'Parametrization': 'PARAMETRIZATION', 'Scale_c': 'SCALE_C'}
        self._attributes = ['Section_parameters']

