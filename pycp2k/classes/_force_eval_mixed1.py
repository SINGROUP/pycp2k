from pycp2k.inputsection import InputSection
from ._fragment1 import _fragment1


class _force_eval_mixed1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.FRAGMENT_list = []
        self._name = "FORCE_EVAL_MIXED"
        self._repeated_subsections = {'FRAGMENT': '_fragment1'}
        self._attributes = ['FRAGMENT_list']

    def FRAGMENT_add(self, section_parameters=None):
        new_section = _fragment1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FRAGMENT_list.append(new_section)
        return new_section

