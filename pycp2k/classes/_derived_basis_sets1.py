from pycp2k.inputsection import InputSection


class _derived_basis_sets1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Basis_set_name = None
        self.Reference_set = None
        self.Remove_contraction = []
        self.Remove_set = []
        self._name = "DERIVED_BASIS_SETS"
        self._keywords = {'Basis_set_name': 'BASIS_SET_NAME', 'Reference_set': 'REFERENCE_SET'}
        self._repeated_keywords = {'Remove_set': 'REMOVE_SET', 'Remove_contraction': 'REMOVE_CONTRACTION'}

