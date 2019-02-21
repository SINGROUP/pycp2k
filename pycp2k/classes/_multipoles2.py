from pycp2k.inputsection import InputSection


class _multipoles2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_multipole_expansion = None
        self.Pol_scf = None
        self.Max_ipol_iter = None
        self.Eps_pol = None
        self._name = "MULTIPOLES"
        self._keywords = {'Max_ipol_iter': 'MAX_IPOL_ITER', 'Max_multipole_expansion': 'MAX_MULTIPOLE_EXPANSION', 'Eps_pol': 'EPS_POL', 'Pol_scf': 'POL_SCF'}
        self._attributes = ['Section_parameters']

