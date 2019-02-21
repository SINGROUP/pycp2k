from pycp2k.inputsection import InputSection


class _lyp_adiabatic3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Lambda = None
        self._name = "LYP_ADIABATIC"
        self._keywords = {'Lambda': 'LAMBDA'}
        self._attributes = ['Section_parameters']

