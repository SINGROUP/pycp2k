from pycp2k.inputsection import InputSection
from ._trajectory1 import _trajectory1
from ._shell_trajectory1 import _shell_trajectory1
from ._core_trajectory1 import _core_trajectory1
from ._cell2 import _cell2
from ._velocities1 import _velocities1
from ._shell_velocities1 import _shell_velocities1
from ._core_velocities1 import _core_velocities1
from ._structure_data1 import _structure_data1
from ._force_mixing_labels1 import _force_mixing_labels1
from ._forces2 import _forces2
from ._shell_forces1 import _shell_forces1
from ._core_forces1 import _core_forces1
from ._mixed_energies1 import _mixed_energies1
from ._stress1 import _stress1
from ._restart5 import _restart5
from ._restart_history1 import _restart_history1
from ._translation_vector1 import _translation_vector1


class _print16(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.TRAJECTORY = _trajectory1()
        self.SHELL_TRAJECTORY = _shell_trajectory1()
        self.CORE_TRAJECTORY = _core_trajectory1()
        self.CELL = _cell2()
        self.VELOCITIES = _velocities1()
        self.SHELL_VELOCITIES = _shell_velocities1()
        self.CORE_VELOCITIES = _core_velocities1()
        self.STRUCTURE_DATA = _structure_data1()
        self.FORCE_MIXING_LABELS = _force_mixing_labels1()
        self.FORCES = _forces2()
        self.SHELL_FORCES = _shell_forces1()
        self.CORE_FORCES = _core_forces1()
        self.MIXED_ENERGIES = _mixed_energies1()
        self.STRESS = _stress1()
        self.RESTART = _restart5()
        self.RESTART_HISTORY = _restart_history1()
        self.TRANSLATION_VECTOR = _translation_vector1()
        self._name = "PRINT"
        self._subsections = {'CORE_FORCES': 'CORE_FORCES', 'MIXED_ENERGIES': 'MIXED_ENERGIES', 'FORCES': 'FORCES', 'TRANSLATION_VECTOR': 'TRANSLATION_VECTOR', 'RESTART_HISTORY': 'RESTART_HISTORY', 'FORCE_MIXING_LABELS': 'FORCE_MIXING_LABELS', 'SHELL_FORCES': 'SHELL_FORCES', 'TRAJECTORY': 'TRAJECTORY', 'CORE_TRAJECTORY': 'CORE_TRAJECTORY', 'CELL': 'CELL', 'SHELL_TRAJECTORY': 'SHELL_TRAJECTORY', 'STRUCTURE_DATA': 'STRUCTURE_DATA', 'SHELL_VELOCITIES': 'SHELL_VELOCITIES', 'VELOCITIES': 'VELOCITIES', 'CORE_VELOCITIES': 'CORE_VELOCITIES', 'STRESS': 'STRESS', 'RESTART': 'RESTART'}

