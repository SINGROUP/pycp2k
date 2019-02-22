from pycp2k.inputsection import InputSection


class _buck4ranges1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.A = None
        self.B = None
        self.C = None
        self.R1 = None
        self.R2 = None
        self.R3 = None
        self.Poly1 = []
        self.Poly2 = []
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "BUCK4RANGES"
        self._keywords = {'Rmax': 'RMAX', 'Atoms': 'ATOMS', 'R2': 'R2', 'A': 'A', 'Rcut': 'RCUT', 'R3': 'R3', 'R1': 'R1', 'C': 'C', 'B': 'B', 'Rmin': 'RMIN'}
        self._repeated_keywords = {'Poly2': 'POLY2', 'Poly1': 'POLY1'}

