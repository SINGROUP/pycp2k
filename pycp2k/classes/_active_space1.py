from pycp2k.inputsection import InputSection
from ._fcidump1 import _fcidump1
from ._print_orbital_cubes1 import _print_orbital_cubes1
from ._eri1 import _eri1
from ._eri_gpw1 import _eri_gpw1
from ._localize3 import _localize3


class _active_space1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Model = None
        self.Active_electrons = None
        self.Inactive_electrons = None
        self.Active_orbitals = None
        self.Inactive_orbitals = None
        self.Isolated_system = None
        self.Orbital_selection = None
        self.Subspace_atom = None
        self.Subspace_shell = None
        self.FCIDUMP = _fcidump1()
        self.PRINT_ORBITAL_CUBES = _print_orbital_cubes1()
        self.ERI = _eri1()
        self.ERI_GPW = _eri_gpw1()
        self.LOCALIZE = _localize3()
        self._name = "ACTIVE_SPACE"
        self._keywords = {'Subspace_atom': 'SUBSPACE_ATOM', 'Isolated_system': 'ISOLATED_SYSTEM', 'Active_electrons': 'ACTIVE_ELECTRONS', 'Active_orbitals': 'ACTIVE_ORBITALS', 'Inactive_orbitals': 'INACTIVE_ORBITALS', 'Orbital_selection': 'ORBITAL_SELECTION', 'Subspace_shell': 'SUBSPACE_SHELL', 'Model': 'MODEL', 'Inactive_electrons': 'INACTIVE_ELECTRONS'}
        self._subsections = {'PRINT_ORBITAL_CUBES': 'PRINT_ORBITAL_CUBES', 'LOCALIZE': 'LOCALIZE', 'FCIDUMP': 'FCIDUMP', 'ERI_GPW': 'ERI_GPW', 'ERI': 'ERI'}
        self._attributes = ['Section_parameters']

