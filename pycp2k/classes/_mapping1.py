from pycp2k.inputsection import InputSection
from ._force_eval_mixed1 import _force_eval_mixed1
from ._force_eval1 import _force_eval1


class _mapping1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.FORCE_EVAL_MIXED_list = []
        self.FORCE_EVAL_list = []
        self._name = "MAPPING"
        self._repeated_subsections = {'FORCE_EVAL_MIXED': '_force_eval_mixed1', 'FORCE_EVAL': '_force_eval1'}
        self._attributes = ['FORCE_EVAL_MIXED_list', 'FORCE_EVAL_list']

    def FORCE_EVAL_MIXED_add(self, section_parameters=None):
        new_section = _force_eval_mixed1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCE_EVAL_MIXED_list.append(new_section)
        return new_section

    def FORCE_EVAL_add(self, section_parameters=None):
        new_section = _force_eval1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCE_EVAL_list.append(new_section)
        return new_section

