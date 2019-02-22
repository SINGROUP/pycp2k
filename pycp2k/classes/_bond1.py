from pycp2k.inputsection import InputSection


class _bond1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Kind = None
        self.K = None
        self.Cs = None
        self.R0 = None
        self._name = "BOND"
        self._keywords = {'Atoms': 'ATOMS', 'Cs': 'CS', 'Kind': 'KIND', 'K': 'K', 'R0': 'R0'}

