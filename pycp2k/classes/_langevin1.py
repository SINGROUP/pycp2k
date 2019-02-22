from pycp2k.inputsection import InputSection


class _langevin1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Gamma = None
        self.Noisy_gamma = None
        self.Shadow_gamma = None
        self._name = "LANGEVIN"
        self._keywords = {'Noisy_gamma': 'NOISY_GAMMA', 'Gamma': 'GAMMA', 'Shadow_gamma': 'SHADOW_GAMMA'}
        self._aliases = {'Noisygamma': 'Noisy_gamma', 'Shadowgamma': 'Shadow_gamma'}


    @property
    def Noisygamma(self):
        """
        See documentation for Noisy_gamma
        """
        return self.Noisy_gamma

    @property
    def Shadowgamma(self):
        """
        See documentation for Shadow_gamma
        """
        return self.Shadow_gamma

    @Noisygamma.setter
    def Noisygamma(self, value):
        self.Noisy_gamma = value

    @Shadowgamma.setter
    def Shadowgamma(self, value):
        self.Shadow_gamma = value
