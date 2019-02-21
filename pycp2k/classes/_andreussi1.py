from pycp2k.inputsection import InputSection


class _andreussi1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rho_max = None
        self.Rho_min = None
        self._name = "ANDREUSSI"
        self._keywords = {'Rho_max': 'RHO_MAX', 'Rho_min': 'RHO_MIN'}

