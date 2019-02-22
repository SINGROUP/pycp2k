from pycp2k.inputsection import InputSection
from ._define_region4 import _define_region4
from ._nose5 import _nose5


class _thermostat_slow1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Region = None
        self.DEFINE_REGION_list = []
        self.NOSE = _nose5()
        self._name = "THERMOSTAT_SLOW"
        self._keywords = {'Region': 'REGION', 'Type': 'TYPE'}
        self._subsections = {'NOSE': 'NOSE'}
        self._repeated_subsections = {'DEFINE_REGION': '_define_region4'}
        self._attributes = ['DEFINE_REGION_list']

    def DEFINE_REGION_add(self, section_parameters=None):
        new_section = _define_region4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DEFINE_REGION_list.append(new_section)
        return new_section

