from pycp2k.inputsection import InputSection


class _constrain_exponents2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Use_exp = None
        self.Boundaries = None
        self.Max_var_fraction = None
        self._name = "CONSTRAIN_EXPONENTS"
        self._keywords = {'Boundaries': 'BOUNDARIES', 'Max_var_fraction': 'MAX_VAR_FRACTION', 'Use_exp': 'USE_EXP'}

