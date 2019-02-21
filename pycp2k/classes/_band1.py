from pycp2k.inputsection import InputSection
from ._convergence_control2 import _convergence_control2
from ._ci_neb1 import _ci_neb1
from ._string_method1 import _string_method1
from ._optimize_band1 import _optimize_band1
from ._replica1 import _replica1
from ._program_run_info10 import _program_run_info10
from ._convergence_info1 import _convergence_info1
from ._replica_info1 import _replica_info1
from ._energy8 import _energy8
from ._banner1 import _banner1


class _band1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nproc_rep = None
        self.Proc_dist_type = None
        self.Band_type = None
        self.Number_of_replica = None
        self.Use_colvars = None
        self.Pot_type = None
        self.Rotate_frames = None
        self.Align_frames = None
        self.K_spring = None
        self.CONVERGENCE_CONTROL = _convergence_control2()
        self.CI_NEB = _ci_neb1()
        self.STRING_METHOD = _string_method1()
        self.OPTIMIZE_BAND_list = []
        self.REPLICA_list = []
        self.PROGRAM_RUN_INFO = _program_run_info10()
        self.CONVERGENCE_INFO = _convergence_info1()
        self.REPLICA_INFO = _replica_info1()
        self.ENERGY = _energy8()
        self.BANNER = _banner1()
        self._name = "BAND"
        self._keywords = {'Proc_dist_type': 'PROC_DIST_TYPE', 'Nproc_rep': 'NPROC_REP', 'Pot_type': 'POT_TYPE', 'K_spring': 'K_SPRING', 'Number_of_replica': 'NUMBER_OF_REPLICA', 'Rotate_frames': 'ROTATE_FRAMES', 'Align_frames': 'ALIGN_FRAMES', 'Use_colvars': 'USE_COLVARS', 'Band_type': 'BAND_TYPE'}
        self._subsections = {'BANNER': 'BANNER', 'REPLICA_INFO': 'REPLICA_INFO', 'ENERGY': 'ENERGY', 'CI_NEB': 'CI_NEB', 'CONVERGENCE_INFO': 'CONVERGENCE_INFO', 'STRING_METHOD': 'STRING_METHOD', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'CONVERGENCE_CONTROL': 'CONVERGENCE_CONTROL'}
        self._repeated_subsections = {'REPLICA': '_replica1', 'OPTIMIZE_BAND': '_optimize_band1'}
        self._aliases = {'K': 'K_spring'}
        self._attributes = ['OPTIMIZE_BAND_list', 'REPLICA_list']

    def REPLICA_add(self, section_parameters=None):
        new_section = _replica1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.REPLICA_list.append(new_section)
        return new_section

    def OPTIMIZE_BAND_add(self, section_parameters=None):
        new_section = _optimize_band1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.OPTIMIZE_BAND_list.append(new_section)
        return new_section


    @property
    def K(self):
        """
        See documentation for K_spring
        """
        return self.K_spring

    @K.setter
    def K(self, value):
        self.K_spring = value
