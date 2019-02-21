from pycp2k.inputsection import InputSection


class _msst1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pressure = None
        self.Energy = None
        self.Volume = None
        self.Cmass = None
        self.Vshock = None
        self.Gamma = None
        self._name = "MSST"
        self._keywords = {'Gamma': 'GAMMA', 'Energy': 'ENERGY', 'Volume': 'VOLUME', 'Cmass': 'CMASS', 'Vshock': 'VSHOCK', 'Pressure': 'PRESSURE'}
        self._aliases = {'V_shock': 'Vshock'}


    @property
    def V_shock(self):
        """
        See documentation for Vshock
        """
        return self.Vshock

    @V_shock.setter
    def V_shock(self, value):
        self.Vshock = value
