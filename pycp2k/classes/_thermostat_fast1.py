from pycp2k.inputsection import InputSection
from ._define_region3 import _define_region3
from ._nose4 import _nose4


class _thermostat_fast1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Region = None
        self.DEFINE_REGION_list = []
        self.NOSE = _nose4()
        self._name = "THERMOSTAT_FAST"
        self._keywords = {'Region': 'REGION', 'Type': 'TYPE'}
        self._subsections = {'NOSE': 'NOSE'}
        self._repeated_subsections = {'DEFINE_REGION': '_define_region3'}
        self._attributes = ['DEFINE_REGION_list']

    def DEFINE_REGION_add(self, section_parameters=None):
        new_section = _define_region3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DEFINE_REGION_list.append(new_section)
        return new_section

