from pycp2k.inputsection import InputSection
from ._energies1 import _energies1
from ._energies_var1 import _energies_var1
from ._forces3 import _forces3
from ._coord_avg1 import _coord_avg1
from ._coord_var1 import _coord_var1
from ._count1 import _count1


class _print45(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ENERGIES = _energies1()
        self.ENERGIES_VAR = _energies_var1()
        self.FORCES = _forces3()
        self.COORD_AVG = _coord_avg1()
        self.COORD_VAR = _coord_var1()
        self.COUNT = _count1()
        self._name = "PRINT"
        self._subsections = {'COORD_AVG': 'COORD_AVG', 'COORD_VAR': 'COORD_VAR', 'FORCES': 'FORCES', 'ENERGIES': 'ENERGIES', 'ENERGIES_VAR': 'ENERGIES_VAR', 'COUNT': 'COUNT'}

