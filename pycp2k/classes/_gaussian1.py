from pycp2k.inputsection import InputSection


class _gaussian1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ww = None
        self.Sigma = None
        self._name = "GAUSSIAN"
        self._keywords = {'Sigma': 'SIGMA', 'Ww': 'WW'}

