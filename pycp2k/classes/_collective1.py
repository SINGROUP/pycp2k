from pycp2k.inputsection import InputSection
from ._restraint5 import _restraint5


class _collective1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Colvar = None
        self.Molecule = None
        self.Molname = None
        self.Intermolecular = None
        self.Target = None
        self.Target_growth = None
        self.Target_limit = None
        self.Exclude_qm = None
        self.Exclude_mm = None
        self.RESTRAINT = _restraint5()
        self._name = "COLLECTIVE"
        self._keywords = {'Molname': 'MOLNAME', 'Exclude_qm': 'EXCLUDE_QM', 'Colvar': 'COLVAR', 'Target_limit': 'TARGET_LIMIT', 'Target': 'TARGET', 'Target_growth': 'TARGET_GROWTH', 'Intermolecular': 'INTERMOLECULAR', 'Molecule': 'MOLECULE', 'Exclude_mm': 'EXCLUDE_MM'}
        self._subsections = {'RESTRAINT': 'RESTRAINT'}
        self._aliases = {'Segname': 'Molname'}


    @property
    def Segname(self):
        """
        See documentation for Molname
        """
        return self.Molname

    @Segname.setter
    def Segname(self, value):
        self.Molname = value
