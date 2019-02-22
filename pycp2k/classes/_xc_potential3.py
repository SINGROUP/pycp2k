from pycp2k.inputsection import InputSection
from ._saop3 import _saop3


class _xc_potential3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Energy = None
        self.SAOP_list = []
        self._name = "XC_POTENTIAL"
        self._keywords = {'Energy': 'ENERGY'}
        self._repeated_subsections = {'SAOP': '_saop3'}
        self._attributes = ['SAOP_list']

    def SAOP_add(self, section_parameters=None):
        new_section = _saop3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.SAOP_list.append(new_section)
        return new_section

