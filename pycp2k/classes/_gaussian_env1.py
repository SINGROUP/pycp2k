from pycp2k.inputsection import InputSection


class _gaussian_env1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.T0 = None
        self.Sigma = None
        self._name = "GAUSSIAN_ENV"
        self._keywords = {'T0': 'T0', 'Sigma': 'SIGMA'}

