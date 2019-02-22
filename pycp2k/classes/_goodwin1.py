from pycp2k.inputsection import InputSection


class _goodwin1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Vr0 = None
        self.D = None
        self.Dc = None
        self.M = None
        self.Mc = None
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "GOODWIN"
        self._keywords = {'Atoms': 'ATOMS', 'Dc': 'DC', 'Mc': 'MC', 'Vr0': 'VR0', 'Rcut': 'RCUT', 'M': 'M', 'Rmax': 'RMAX', 'D': 'D', 'Rmin': 'RMIN'}

