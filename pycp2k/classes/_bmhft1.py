from pycp2k.inputsection import InputSection


class _bmhft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Map_atoms = None
        self.Rcut = None
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.Rmin = None
        self.Rmax = None
        self._name = "BMHFT"
        self._keywords = {'Atoms': 'ATOMS', 'Rmax': 'RMAX', 'A': 'A', 'Rcut': 'RCUT', 'Map_atoms': 'MAP_ATOMS', 'C': 'C', 'B': 'B', 'Rmin': 'RMIN', 'D': 'D'}

