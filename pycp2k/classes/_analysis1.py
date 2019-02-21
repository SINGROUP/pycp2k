from pycp2k.inputsection import InputSection
from ._print22 import _print22


class _analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Frozen_mo_energy_term = None
        self.PRINT_list = []
        self._name = "ANALYSIS"
        self._keywords = {'Frozen_mo_energy_term': 'FROZEN_MO_ENERGY_TERM'}
        self._repeated_subsections = {'PRINT': '_print22'}
        self._attributes = ['Section_parameters', 'PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print22()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

