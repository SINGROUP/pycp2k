from pycp2k.inputsection import InputSection


class _ub1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Kind = None
        self.K = None
        self.Cs = None
        self.R0 = None
        self._name = "UB"
        self._keywords = {'Cs': 'CS', 'Kind': 'KIND', 'K': 'K', 'R0': 'R0'}

