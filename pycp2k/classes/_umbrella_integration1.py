from pycp2k.inputsection import InputSection
from ._convergence_control1 import _convergence_control1
from ._uvar1 import _uvar1


class _umbrella_integration1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.CONVERGENCE_CONTROL_list = []
        self.UVAR_list = []
        self._name = "UMBRELLA_INTEGRATION"
        self._repeated_subsections = {'UVAR': '_uvar1', 'CONVERGENCE_CONTROL': '_convergence_control1'}
        self._attributes = ['CONVERGENCE_CONTROL_list', 'UVAR_list']

    def UVAR_add(self, section_parameters=None):
        new_section = _uvar1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.UVAR_list.append(new_section)
        return new_section

    def CONVERGENCE_CONTROL_add(self, section_parameters=None):
        new_section = _convergence_control1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONVERGENCE_CONTROL_list.append(new_section)
        return new_section

