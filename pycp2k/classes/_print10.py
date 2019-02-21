from pycp2k.inputsection import InputSection
from ._msd_kind1 import _msd_kind1
from ._msd_molecule1 import _msd_molecule1
from ._displaced_atom1 import _displaced_atom1


class _print10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MSD_KIND = _msd_kind1()
        self.MSD_MOLECULE = _msd_molecule1()
        self.DISPLACED_ATOM = _displaced_atom1()
        self._name = "PRINT"
        self._subsections = {'DISPLACED_ATOM': 'DISPLACED_ATOM', 'MSD_MOLECULE': 'MSD_MOLECULE', 'MSD_KIND': 'MSD_KIND'}

