from pycp2k.inputsection import InputSection
from ._atomic_coordinates1 import _atomic_coordinates1
from ._structure_data2 import _structure_data2
from ._interatomic_distances1 import _interatomic_distances1
from ._topology_info1 import _topology_info1
from ._cell5 import _cell5
from ._kinds1 import _kinds1
from ._symmetry1 import _symmetry1
from ._molecules1 import _molecules1
from ._radii1 import _radii1


class _print52(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ATOMIC_COORDINATES = _atomic_coordinates1()
        self.STRUCTURE_DATA = _structure_data2()
        self.INTERATOMIC_DISTANCES = _interatomic_distances1()
        self.TOPOLOGY_INFO = _topology_info1()
        self.CELL = _cell5()
        self.KINDS = _kinds1()
        self.SYMMETRY = _symmetry1()
        self.MOLECULES = _molecules1()
        self.RADII = _radii1()
        self._name = "PRINT"
        self._subsections = {'RADII': 'RADII', 'ATOMIC_COORDINATES': 'ATOMIC_COORDINATES', 'CELL': 'CELL', 'KINDS': 'KINDS', 'STRUCTURE_DATA': 'STRUCTURE_DATA', 'SYMMETRY': 'SYMMETRY', 'TOPOLOGY_INFO': 'TOPOLOGY_INFO', 'INTERATOMIC_DISTANCES': 'INTERATOMIC_DISTANCES', 'MOLECULES': 'MOLECULES'}

