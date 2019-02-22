from pycp2k.inputsection import InputSection
from ._program_run_info22 import _program_run_info22
from ._wannier_cubes1 import _wannier_cubes1
from ._wannier_centers1 import _wannier_centers1
from ._wannier_spreads1 import _wannier_spreads1
from ._loc_restart1 import _loc_restart1
from ._total_dipole1 import _total_dipole1
from ._molecular_dipoles1 import _molecular_dipoles1
from ._molecular_states1 import _molecular_states1
from ._wannier_states1 import _wannier_states1


class _print34(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info22()
        self.WANNIER_CUBES = _wannier_cubes1()
        self.WANNIER_CENTERS = _wannier_centers1()
        self.WANNIER_SPREADS = _wannier_spreads1()
        self.LOC_RESTART = _loc_restart1()
        self.TOTAL_DIPOLE = _total_dipole1()
        self.MOLECULAR_DIPOLES = _molecular_dipoles1()
        self.MOLECULAR_STATES = _molecular_states1()
        self.WANNIER_STATES = _wannier_states1()
        self._name = "PRINT"
        self._subsections = {'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'LOC_RESTART': 'LOC_RESTART', 'WANNIER_STATES': 'WANNIER_STATES', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES'}

