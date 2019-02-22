from pycp2k.inputsection import InputSection


class _mom2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Start_iter = None
        self.Deocc_alpha = None
        self.Deocc_beta = None
        self.Occ_alpha = None
        self.Occ_beta = None
        self.Proj_formula = None
        self._name = "MOM"
        self._keywords = {'Occ_alpha': 'OCC_ALPHA', 'Deocc_alpha': 'DEOCC_ALPHA', 'Occ_beta': 'OCC_BETA', 'Start_iter': 'START_ITER', 'Deocc_beta': 'DEOCC_BETA', 'Proj_formula': 'PROJ_FORMULA'}
        self._attributes = ['Section_parameters']

