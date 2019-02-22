from pycp2k.inputsection import InputSection
from ._define_region2 import _define_region2
from ._nose3 import _nose3
from ._csvr3 import _csvr3
from ._gle3 import _gle3
from ._ad_langevin3 import _ad_langevin3
from ._print9 import _print9


class _thermostat3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Region = None
        self.DEFINE_REGION_list = []
        self.NOSE = _nose3()
        self.CSVR = _csvr3()
        self.GLE = _gle3()
        self.AD_LANGEVIN = _ad_langevin3()
        self.PRINT = _print9()
        self._name = "THERMOSTAT"
        self._keywords = {'Region': 'REGION', 'Type': 'TYPE'}
        self._subsections = {'AD_LANGEVIN': 'AD_LANGEVIN', 'NOSE': 'NOSE', 'GLE': 'GLE', 'CSVR': 'CSVR', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'DEFINE_REGION': '_define_region2'}
        self._attributes = ['DEFINE_REGION_list']

    def DEFINE_REGION_add(self, section_parameters=None):
        new_section = _define_region2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DEFINE_REGION_list.append(new_section)
        return new_section

