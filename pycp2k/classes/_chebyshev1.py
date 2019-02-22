from pycp2k.inputsection import InputSection
from ._dos1 import _dos1
from ._print_specific_e_density_cube1 import _print_specific_e_density_cube1


class _chebyshev1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_chebyshev = None
        self.DOS = _dos1()
        self.PRINT_SPECIFIC_E_DENSITY_CUBE = _print_specific_e_density_cube1()
        self._name = "CHEBYSHEV"
        self._keywords = {'N_chebyshev': 'N_CHEBYSHEV'}
        self._subsections = {'DOS': 'DOS', 'PRINT_SPECIFIC_E_DENSITY_CUBE': 'PRINT_SPECIFIC_E_DENSITY_CUBE'}

