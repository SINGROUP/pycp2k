from pycp2k.inputsection import InputSection


class _hydronium_distance2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Oxygens = []
        self.Hydrogens = []
        self.Roh = None
        self.Poh = None
        self.Qoh = None
        self.Nh = None
        self.Pm = None
        self.Qm = None
        self.Nn = None
        self.Pf = None
        self.Qf = None
        self.Lambda = None
        self._name = "HYDRONIUM_DISTANCE"
        self._keywords = {'Qm': 'QM', 'Qoh': 'QOH', 'Roh': 'ROH', 'Poh': 'POH', 'Lambda': 'LAMBDA', 'Pf': 'PF', 'Nn': 'NN', 'Nh': 'NH', 'Pm': 'PM', 'Qf': 'QF'}
        self._repeated_keywords = {'Hydrogens': 'HYDROGENS', 'Oxygens': 'OXYGENS'}

