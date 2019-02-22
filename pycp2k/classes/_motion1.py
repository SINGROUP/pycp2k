from pycp2k.inputsection import InputSection
from ._geo_opt1 import _geo_opt1
from ._cell_opt1 import _cell_opt1
from ._shell_opt1 import _shell_opt1
from ._md1 import _md1
from ._driver1 import _driver1
from ._free_energy1 import _free_energy1
from ._constraint1 import _constraint1
from ._flexible_partitioning1 import _flexible_partitioning1
from ._mc1 import _mc1
from ._tmc1 import _tmc1
from ._pint1 import _pint1
from ._band1 import _band1
from ._print16 import _print16


class _motion1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.GEO_OPT = _geo_opt1()
        self.CELL_OPT = _cell_opt1()
        self.SHELL_OPT = _shell_opt1()
        self.MD = _md1()
        self.DRIVER = _driver1()
        self.FREE_ENERGY = _free_energy1()
        self.CONSTRAINT = _constraint1()
        self.FLEXIBLE_PARTITIONING = _flexible_partitioning1()
        self.MC = _mc1()
        self.TMC = _tmc1()
        self.PINT = _pint1()
        self.BAND = _band1()
        self.PRINT_list = []
        self._name = "MOTION"
        self._subsections = {'TMC': 'TMC', 'FREE_ENERGY': 'FREE_ENERGY', 'CELL_OPT': 'CELL_OPT', 'CONSTRAINT': 'CONSTRAINT', 'SHELL_OPT': 'SHELL_OPT', 'GEO_OPT': 'GEO_OPT', 'MD': 'MD', 'DRIVER': 'DRIVER', 'BAND': 'BAND', 'PINT': 'PINT', 'FLEXIBLE_PARTITIONING': 'FLEXIBLE_PARTITIONING', 'MC': 'MC'}
        self._repeated_subsections = {'PRINT': '_print16'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print16()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

