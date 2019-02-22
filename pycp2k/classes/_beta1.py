from pycp2k.inputsection import InputSection


class _beta1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nel = None
        self.L = None
        self.N = None
        self._name = "BETA"
        self._keywords = {'N': 'N', 'Nel': 'NEL', 'L': 'L'}

