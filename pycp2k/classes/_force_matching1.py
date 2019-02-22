from pycp2k.inputsection import InputSection
from ._compare_energies1 import _compare_energies1
from ._compare_forces1 import _compare_forces1


class _force_matching1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Optimize_file_name = None
        self.Ref_traj_file_name = None
        self.Ref_force_file_name = None
        self.Ref_cell_file_name = None
        self.Group_size = None
        self.Frame_start = None
        self.Frame_stop = None
        self.Frame_stride = None
        self.Frame_count = None
        self.Energy_weight = None
        self.Shift_average = None
        self.Shift_qm = None
        self.Shift_mm = None
        self.COMPARE_ENERGIES = _compare_energies1()
        self.COMPARE_FORCES = _compare_forces1()
        self._name = "FORCE_MATCHING"
        self._keywords = {'Ref_force_file_name': 'REF_FORCE_FILE_NAME', 'Ref_cell_file_name': 'REF_CELL_FILE_NAME', 'Frame_start': 'FRAME_START', 'Optimize_file_name': 'OPTIMIZE_FILE_NAME', 'Shift_average': 'SHIFT_AVERAGE', 'Ref_traj_file_name': 'REF_TRAJ_FILE_NAME', 'Frame_stride': 'FRAME_STRIDE', 'Shift_qm': 'SHIFT_QM', 'Frame_stop': 'FRAME_STOP', 'Frame_count': 'FRAME_COUNT', 'Shift_mm': 'SHIFT_MM', 'Group_size': 'GROUP_SIZE', 'Energy_weight': 'ENERGY_WEIGHT'}
        self._subsections = {'COMPARE_FORCES': 'COMPARE_FORCES', 'COMPARE_ENERGIES': 'COMPARE_ENERGIES'}

