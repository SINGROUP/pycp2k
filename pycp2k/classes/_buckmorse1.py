from pycp2k.inputsection import InputSection


class _buckmorse1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.F0 = None
        self.A1 = None
        self.A2 = None
        self.B1 = None
        self.B2 = None
        self.C = None
        self.D = None
        self.R0 = None
        self.Beta = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "BUCKMORSE"
        self._keywords = {'F0': 'F0', 'A2': 'A2', 'Rmax': 'RMAX', 'C': 'C', 'B2': 'B2', 'Beta': 'BETA', 'A1': 'A1', 'Atoms': 'ATOMS', 'Rcut': 'RCUT', 'B1': 'B1', 'D': 'D', 'Rmin': 'RMIN', 'R0': 'R0'}

