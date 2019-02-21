from pycp2k.inputsection import InputSection


class _lennard_jones2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Epsilon = None
        self.Sigma = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "LENNARD-JONES"
        self._keywords = {'Atoms': 'ATOMS', 'Sigma': 'SIGMA', 'Rcut': 'RCUT', 'Epsilon': 'EPSILON', 'Rmax': 'RMAX', 'Rmin': 'RMIN'}

