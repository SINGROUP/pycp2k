from pycp2k.inputsection import InputSection
from ._program_run_info39 import _program_run_info39
from ._wannier_cubes5 import _wannier_cubes5
from ._wannier_centers5 import _wannier_centers5
from ._wannier_spreads5 import _wannier_spreads5
from ._loc_restart5 import _loc_restart5
from ._total_dipole4 import _total_dipole4
from ._molecular_dipoles4 import _molecular_dipoles4
from ._molecular_states4 import _molecular_states4
from ._wannier_states4 import _wannier_states4


class _print53(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info39()
        self.WANNIER_CUBES = _wannier_cubes5()
        self.WANNIER_CENTERS = _wannier_centers5()
        self.WANNIER_SPREADS = _wannier_spreads5()
        self.LOC_RESTART = _loc_restart5()
        self.TOTAL_DIPOLE = _total_dipole4()
        self.MOLECULAR_DIPOLES = _molecular_dipoles4()
        self.MOLECULAR_STATES = _molecular_states4()
        self.WANNIER_STATES = _wannier_states4()
        self._name = "PRINT"
        self._subsections = {'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'LOC_RESTART': 'LOC_RESTART', 'WANNIER_STATES': 'WANNIER_STATES', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES'}

