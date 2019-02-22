from pycp2k.inputsection import InputSection
from ._program_run_info24 import _program_run_info24
from ._wannier_cubes3 import _wannier_cubes3
from ._wannier_centers3 import _wannier_centers3
from ._wannier_spreads3 import _wannier_spreads3
from ._loc_restart3 import _loc_restart3
from ._total_dipole2 import _total_dipole2
from ._molecular_dipoles2 import _molecular_dipoles2
from ._molecular_states2 import _molecular_states2
from ._wannier_states2 import _wannier_states2


class _print36(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info24()
        self.WANNIER_CUBES = _wannier_cubes3()
        self.WANNIER_CENTERS = _wannier_centers3()
        self.WANNIER_SPREADS = _wannier_spreads3()
        self.LOC_RESTART = _loc_restart3()
        self.TOTAL_DIPOLE = _total_dipole2()
        self.MOLECULAR_DIPOLES = _molecular_dipoles2()
        self.MOLECULAR_STATES = _molecular_states2()
        self.WANNIER_STATES = _wannier_states2()
        self._name = "PRINT"
        self._subsections = {'MOLECULAR_DIPOLES': 'MOLECULAR_DIPOLES', 'TOTAL_DIPOLE': 'TOTAL_DIPOLE', 'LOC_RESTART': 'LOC_RESTART', 'WANNIER_STATES': 'WANNIER_STATES', 'MOLECULAR_STATES': 'MOLECULAR_STATES', 'WANNIER_CENTERS': 'WANNIER_CENTERS', 'WANNIER_SPREADS': 'WANNIER_SPREADS', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'WANNIER_CUBES': 'WANNIER_CUBES'}

