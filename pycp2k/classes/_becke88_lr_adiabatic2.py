from pycp2k.inputsection import InputSection


class _becke88_lr_adiabatic2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Scale_x = None
        self.Omega = None
        self.Lambda = None
        self._name = "BECKE88_LR_ADIABATIC"
        self._keywords = {'Omega': 'OMEGA', 'Scale_x': 'SCALE_X', 'Lambda': 'LAMBDA'}
        self._attributes = ['Section_parameters']

