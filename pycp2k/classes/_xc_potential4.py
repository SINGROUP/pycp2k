from pycp2k.inputsection import InputSection
from ._saop4 import _saop4


class _xc_potential4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Energy = None
        self.SAOP_list = []
        self._name = "XC_POTENTIAL"
        self._keywords = {'Energy': 'ENERGY'}
        self._repeated_subsections = {'SAOP': '_saop4'}
        self._attributes = ['SAOP_list']

    def SAOP_add(self, section_parameters=None):
        new_section = _saop4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.SAOP_list.append(new_section)
        return new_section

