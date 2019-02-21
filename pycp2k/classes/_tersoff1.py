from pycp2k.inputsection import InputSection


class _tersoff1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.A = None
        self.B = None
        self.Lambda1 = None
        self.Lambda2 = None
        self.Alpha = None
        self.Beta = None
        self.N = None
        self.C = None
        self.D = None
        self.H = None
        self.Lambda3 = None
        self.Bigr = None
        self.Bigd = None
        self.Rcut = None
        self._name = "TERSOFF"
        self._keywords = {'Lambda3': 'LAMBDA3', 'B': 'B', 'Bigd': 'BIGD', 'Lambda2': 'LAMBDA2', 'N': 'N', 'C': 'C', 'D': 'D', 'Beta': 'BETA', 'Lambda1': 'LAMBDA1', 'Atoms': 'ATOMS', 'Bigr': 'BIGR', 'A': 'A', 'Alpha': 'ALPHA', 'H': 'H', 'Rcut': 'RCUT'}

