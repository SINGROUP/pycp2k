from pycp2k.inputsection import InputSection
from ._restraint6 import _restraint6


class _fixed_atoms1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Components_to_fix = None
        self.List = []
        self.Molname = []
        self.Segname = self.Molname
        self.Mm_subsys = None
        self.Qm_subsys = None
        self.Exclude_qm = None
        self.Exclude_mm = None
        self.RESTRAINT = _restraint6()
        self._name = "FIXED_ATOMS"
        self._keywords = {'Components_to_fix': 'COMPONENTS_TO_FIX', 'Mm_subsys': 'MM_SUBSYS', 'Qm_subsys': 'QM_SUBSYS', 'Exclude_mm': 'EXCLUDE_MM', 'Exclude_qm': 'EXCLUDE_QM'}
        self._repeated_keywords = {'Molname': 'MOLNAME', 'List': 'LIST'}
        self._subsections = {'RESTRAINT': 'RESTRAINT'}
        self._aliases = {'Protein': 'Mm_subsys'}
        self._repeated_aliases = {'Segname': 'Molname'}


    @property
    def Protein(self):
        """
        See documentation for Mm_subsys
        """
        return self.Mm_subsys

    @Protein.setter
    def Protein(self, value):
        self.Mm_subsys = value
