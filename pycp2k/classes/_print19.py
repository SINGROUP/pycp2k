from pycp2k.inputsection import InputSection
from ._restart6 import _restart6
from ._restart_history2 import _restart_history2
from ._iteration_info1 import _iteration_info1
from ._program_run_info13 import _program_run_info13
from ._mo_orthonormality1 import _mo_orthonormality1
from ._mo_magnitude1 import _mo_magnitude1
from ._detailed_energy1 import _detailed_energy1
from ._diis_info2 import _diis_info2
from ._total_densities1 import _total_densities1
from ._lanczos1 import _lanczos1
from ._diag_sub_scf2 import _diag_sub_scf2
from ._davidson2 import _davidson2
from ._filter_matrix2 import _filter_matrix2
from ._mos_molden1 import _mos_molden1


class _print19(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dm_restart_write = None
        self.RESTART = _restart6()
        self.RESTART_HISTORY = _restart_history2()
        self.ITERATION_INFO = _iteration_info1()
        self.PROGRAM_RUN_INFO = _program_run_info13()
        self.MO_ORTHONORMALITY = _mo_orthonormality1()
        self.MO_MAGNITUDE = _mo_magnitude1()
        self.DETAILED_ENERGY = _detailed_energy1()
        self.DIIS_INFO = _diis_info2()
        self.TOTAL_DENSITIES = _total_densities1()
        self.LANCZOS = _lanczos1()
        self.DIAG_SUB_SCF = _diag_sub_scf2()
        self.DAVIDSON = _davidson2()
        self.FILTER_MATRIX = _filter_matrix2()
        self.MOS_MOLDEN = _mos_molden1()
        self._name = "PRINT"
        self._keywords = {'Dm_restart_write': 'DM_RESTART_WRITE'}
        self._subsections = {'DIAG_SUB_SCF': 'DIAG_SUB_SCF', 'MOS_MOLDEN': 'MOS_MOLDEN', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'FILTER_MATRIX': 'FILTER_MATRIX', 'TOTAL_DENSITIES': 'TOTAL_DENSITIES', 'RESTART_HISTORY': 'RESTART_HISTORY', 'MO_ORTHONORMALITY': 'MO_ORTHONORMALITY', 'DAVIDSON': 'DAVIDSON', 'DIIS_INFO': 'DIIS_INFO', 'MO_MAGNITUDE': 'MO_MAGNITUDE', 'LANCZOS': 'LANCZOS', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'ITERATION_INFO': 'ITERATION_INFO', 'RESTART': 'RESTART'}

