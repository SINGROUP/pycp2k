from pycp2k.inputsection import InputSection
from ._define_region6 import _define_region6
from ._print11 import _print11


class _thermal_region1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Force_rescaling = None
        self.Do_langevin_default = None
        self.DEFINE_REGION_list = []
        self.PRINT = _print11()
        self._name = "THERMAL_REGION"
        self._keywords = {'Force_rescaling': 'FORCE_RESCALING', 'Do_langevin_default': 'DO_LANGEVIN_DEFAULT'}
        self._subsections = {'PRINT': 'PRINT'}
        self._repeated_subsections = {'DEFINE_REGION': '_define_region6'}
        self._attributes = ['DEFINE_REGION_list']

    def DEFINE_REGION_add(self, section_parameters=None):
        new_section = _define_region6()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DEFINE_REGION_list.append(new_section)
        return new_section

