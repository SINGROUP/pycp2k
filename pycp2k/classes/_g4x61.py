from pycp2k.inputsection import InputSection
from ._restraint3 import _restraint3


class _g4x61(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Molecule = None
        self.Molname = None
        self.Intermolecular = None
        self.Atoms = None
        self.Distances = None
        self.Exclude_qm = None
        self.Exclude_mm = None
        self.RESTRAINT = _restraint3()
        self._name = "G4X6"
        self._keywords = {'Molname': 'MOLNAME', 'Exclude_qm': 'EXCLUDE_QM', 'Atoms': 'ATOMS', 'Exclude_mm': 'EXCLUDE_MM', 'Distances': 'DISTANCES', 'Intermolecular': 'INTERMOLECULAR', 'Molecule': 'MOLECULE'}
        self._subsections = {'RESTRAINT': 'RESTRAINT'}
        self._aliases = {'Segname': 'Molname', 'Mol': 'Molecule'}


    @property
    def Mol(self):
        """
        See documentation for Molecule
        """
        return self.Molecule

    @property
    def Segname(self):
        """
        See documentation for Molname
        """
        return self.Molname

    @Mol.setter
    def Mol(self, value):
        self.Molecule = value

    @Segname.setter
    def Segname(self, value):
        self.Molname = value
