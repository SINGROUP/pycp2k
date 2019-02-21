from pycp2k.inputsection import InputSection


class _constraint2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Target = None
        self.Equal_charges = None
        self.Atom_list = []
        self.Atom_coef = None
        self._name = "CONSTRAINT"
        self._keywords = {'Equal_charges': 'EQUAL_CHARGES', 'Atom_coef': 'ATOM_COEF', 'Target': 'TARGET'}
        self._repeated_keywords = {'Atom_list': 'ATOM_LIST'}

