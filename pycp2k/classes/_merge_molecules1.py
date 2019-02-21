from pycp2k.inputsection import InputSection
from ._bonds1 import _bonds1
from ._angles1 import _angles1
from ._torsions1 import _torsions1
from ._impropers1 import _impropers1


class _merge_molecules1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.BONDS = _bonds1()
        self.ANGLES = _angles1()
        self.TORSIONS = _torsions1()
        self.IMPROPERS = _impropers1()
        self._name = "MERGE_MOLECULES"
        self._subsections = {'ANGLES': 'ANGLES', 'TORSIONS': 'TORSIONS', 'BONDS': 'BONDS', 'IMPROPERS': 'IMPROPERS'}

