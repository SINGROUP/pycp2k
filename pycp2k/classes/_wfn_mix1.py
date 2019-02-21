from pycp2k.inputsection import InputSection
from ._update1 import _update1


class _wfn_mix1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Overwrite_mos = None
        self.UPDATE_list = []
        self._name = "WFN_MIX"
        self._keywords = {'Overwrite_mos': 'OVERWRITE_MOS'}
        self._repeated_subsections = {'UPDATE': '_update1'}
        self._attributes = ['UPDATE_list']

    def UPDATE_add(self, section_parameters=None):
        new_section = _update1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.UPDATE_list.append(new_section)
        return new_section

