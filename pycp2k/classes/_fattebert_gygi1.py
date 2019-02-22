from pycp2k.inputsection import InputSection


class _fattebert_gygi1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Beta = None
        self.Rho_zero = None
        self._name = "FATTEBERT-GYGI"
        self._keywords = {'Rho_zero': 'RHO_ZERO', 'Beta': 'BETA'}
        self._aliases = {'Rho0': 'Rho_zero'}


    @property
    def Rho0(self):
        """
        See documentation for Rho_zero
        """
        return self.Rho_zero

    @Rho0.setter
    def Rho0(self, value):
        self.Rho_zero = value
