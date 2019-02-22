from pycp2k.inputsection import InputSection
from ._each200 import _each200
from ._ldos1 import _ldos1
from ._r_ldos1 import _r_ldos1


class _pdos1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Components = None
        self.Append = None
        self.Nlumo = None
        self.Out_each_mo = None
        self.EACH = _each200()
        self.LDOS_list = []
        self.R_LDOS_list = []
        self._name = "PDOS"
        self._keywords = {'Out_each_mo': 'OUT_EACH_MO', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Components': 'COMPONENTS', 'Append': 'APPEND', 'Filename': 'FILENAME', 'Nlumo': 'NLUMO'}
        self._subsections = {'EACH': 'EACH'}
        self._repeated_subsections = {'R_LDOS': '_r_ldos1', 'LDOS': '_ldos1'}
        self._attributes = ['Section_parameters', 'LDOS_list', 'R_LDOS_list']

    def R_LDOS_add(self, section_parameters=None):
        new_section = _r_ldos1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.R_LDOS_list.append(new_section)
        return new_section

    def LDOS_add(self, section_parameters=None):
        new_section = _ldos1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LDOS_list.append(new_section)
        return new_section

