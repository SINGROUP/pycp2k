from pycp2k.inputsection import InputSection
from ._fragment3 import _fragment3
from ._configuration1 import _configuration1
from ._fragment_energies1 import _fragment_energies1
from ._print46 import _print46


class _bsse1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.FRAGMENT_list = []
        self.CONFIGURATION_list = []
        self.FRAGMENT_ENERGIES_list = []
        self.PRINT = _print46()
        self._name = "BSSE"
        self._subsections = {'PRINT': 'PRINT'}
        self._repeated_subsections = {'FRAGMENT': '_fragment3', 'CONFIGURATION': '_configuration1', 'FRAGMENT_ENERGIES': '_fragment_energies1'}
        self._attributes = ['FRAGMENT_list', 'CONFIGURATION_list', 'FRAGMENT_ENERGIES_list']

    def FRAGMENT_add(self, section_parameters=None):
        new_section = _fragment3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FRAGMENT_list.append(new_section)
        return new_section

    def CONFIGURATION_add(self, section_parameters=None):
        new_section = _configuration1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONFIGURATION_list.append(new_section)
        return new_section

    def FRAGMENT_ENERGIES_add(self, section_parameters=None):
        new_section = _fragment_energies1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FRAGMENT_ENERGIES_list.append(new_section)
        return new_section

