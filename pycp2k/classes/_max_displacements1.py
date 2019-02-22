from pycp2k.inputsection import InputSection
from ._mol_displacements1 import _mol_displacements1
from ._box_displacements1 import _box_displacements1


class _max_displacements1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MOL_DISPLACEMENTS = _mol_displacements1()
        self.BOX_DISPLACEMENTS = _box_displacements1()
        self._name = "MAX_DISPLACEMENTS"
        self._subsections = {'BOX_DISPLACEMENTS': 'BOX_DISPLACEMENTS', 'MOL_DISPLACEMENTS': 'MOL_DISPLACEMENTS'}

