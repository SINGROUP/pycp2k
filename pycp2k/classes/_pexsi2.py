from pycp2k.inputsection import InputSection


class _pexsi2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ordering = None
        self.Row_ordering = None
        self.Verbosity = None
        self.Np_symb_fact = None
        self._name = "PEXSI"
        self._keywords = {'Ordering': 'ORDERING', 'Np_symb_fact': 'NP_SYMB_FACT', 'Verbosity': 'VERBOSITY', 'Row_ordering': 'ROW_ORDERING'}

