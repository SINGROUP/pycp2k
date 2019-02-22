from pycp2k.inputsection import InputSection
from ._msd1 import _msd1
from ._print10 import _print10


class _reftraj1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Traj_file_name = None
        self.Cell_file_name = None
        self.Variable_volume = None
        self.First_snapshot = None
        self.Last_snapshot = None
        self.Stride = None
        self.Eval_energy_forces = None
        self.MSD = _msd1()
        self.PRINT = _print10()
        self._name = "REFTRAJ"
        self._keywords = {'Cell_file_name': 'CELL_FILE_NAME', 'Traj_file_name': 'TRAJ_FILE_NAME', 'Eval_energy_forces': 'EVAL_ENERGY_FORCES', 'Variable_volume': 'VARIABLE_VOLUME', 'First_snapshot': 'FIRST_SNAPSHOT', 'Last_snapshot': 'LAST_SNAPSHOT', 'Stride': 'STRIDE'}
        self._subsections = {'MSD': 'MSD', 'PRINT': 'PRINT'}

