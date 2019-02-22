from pycp2k.inputsection import InputSection


class _bmhftd1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Map_atoms = None
        self.Rcut = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.Bd = None
        self.Order = None
        self.Rmin = None
        self.Rmax = None
        self._name = "BMHFTD"
        self._keywords = {'Rmax': 'RMAX', 'Atoms': 'ATOMS', 'Order': 'ORDER', 'A': 'A', 'Rcut': 'RCUT', 'Bd': 'BD', 'Map_atoms': 'MAP_ATOMS', 'C': 'C', 'B': 'B', 'Rmin': 'RMIN', 'D': 'D'}

