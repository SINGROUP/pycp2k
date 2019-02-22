from pycp2k.inputsection import InputSection


class _pw925(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale = None
        self.Parametrization = None
        self._name = "PW92"
        self._keywords = {'Parametrization': 'PARAMETRIZATION', 'Scale': 'SCALE'}
        self._attributes = ['Section_parameters']

