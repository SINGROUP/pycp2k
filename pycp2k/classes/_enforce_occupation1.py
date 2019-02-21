from pycp2k.inputsection import InputSection


class _enforce_occupation1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Orbitals = None
        self.Eps_scf = None
        self.Max_scf = None
        self.Smear = None
        self._name = "ENFORCE_OCCUPATION"
        self._keywords = {'Max_scf': 'MAX_SCF', 'Smear': 'SMEAR', 'Eps_scf': 'EPS_SCF', 'Orbitals': 'ORBITALS'}
        self._aliases = {'M': 'Orbitals'}
        self._attributes = ['Section_parameters']


    @property
    def M(self):
        """
        See documentation for Orbitals
        """
        return self.Orbitals

    @M.setter
    def M(self, value):
        self.Orbitals = value
