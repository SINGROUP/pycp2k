from pycp2k.inputsection import InputSection


class _add_mm_charge1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom_index_1 = None
        self.Atom_index_2 = None
        self.Alpha = None
        self.Radius = None
        self.Corr_radius = None
        self.Charge = None
        self._name = "ADD_MM_CHARGE"
        self._keywords = {'Atom_index_2': 'ATOM_INDEX_2', 'Corr_radius': 'CORR_RADIUS', 'Atom_index_1': 'ATOM_INDEX_1', 'Radius': 'RADIUS', 'Alpha': 'ALPHA', 'Charge': 'CHARGE'}
        self._aliases = {'Mm1': 'Atom_index_1', 'Mm2': 'Atom_index_2'}


    @property
    def Mm1(self):
        """
        See documentation for Atom_index_1
        """
        return self.Atom_index_1

    @property
    def Mm2(self):
        """
        See documentation for Atom_index_2
        """
        return self.Atom_index_2

    @Mm1.setter
    def Mm1(self, value):
        self.Atom_index_1 = value

    @Mm2.setter
    def Mm2(self, value):
        self.Atom_index_2 = value
