from pycp2k.inputsection import InputSection
from ._rng_init10 import _rng_init10
from ._cell4 import _cell4
from ._coord10 import _coord10
from ._velocity10 import _velocity10
from ._kind1 import _kind1
from ._topology1 import _topology1
from ._colvar5 import _colvar5
from ._multipoles4 import _multipoles4
from ._shell_coord1 import _shell_coord1
from ._shell_velocity1 import _shell_velocity1
from ._core_coord1 import _core_coord1
from ._core_velocity1 import _core_velocity1
from ._print52 import _print52


class _subsys1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Seed = None
        self.RNG_INIT = _rng_init10()
        self.CELL = _cell4()
        self.COORD = _coord10()
        self.VELOCITY = _velocity10()
        self.KIND_list = []
        self.TOPOLOGY = _topology1()
        self.COLVAR_list = []
        self.MULTIPOLES = _multipoles4()
        self.SHELL_COORD = _shell_coord1()
        self.SHELL_VELOCITY = _shell_velocity1()
        self.CORE_COORD = _core_coord1()
        self.CORE_VELOCITY = _core_velocity1()
        self.PRINT = _print52()
        self._name = "SUBSYS"
        self._keywords = {'Seed': 'SEED'}
        self._subsections = {'CORE_VELOCITY': 'CORE_VELOCITY', 'RNG_INIT': 'RNG_INIT', 'CELL': 'CELL', 'SHELL_VELOCITY': 'SHELL_VELOCITY', 'VELOCITY': 'VELOCITY', 'CORE_COORD': 'CORE_COORD', 'COORD': 'COORD', 'TOPOLOGY': 'TOPOLOGY', 'SHELL_COORD': 'SHELL_COORD', 'MULTIPOLES': 'MULTIPOLES', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'KIND': '_kind1', 'COLVAR': '_colvar5'}
        self._attributes = ['KIND_list', 'COLVAR_list']

    def KIND_add(self, section_parameters=None):
        new_section = _kind1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KIND_list.append(new_section)
        return new_section

    def COLVAR_add(self, section_parameters=None):
        new_section = _colvar5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.COLVAR_list.append(new_section)
        return new_section

