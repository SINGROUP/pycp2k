from pycp2k.inputsection import InputSection
from ._fragment2 import _fragment2


class _force_eval1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Define_fragments = None
        self.FRAGMENT_list = []
        self._name = "FORCE_EVAL"
        self._keywords = {'Define_fragments': 'DEFINE_FRAGMENTS'}
        self._repeated_subsections = {'FRAGMENT': '_fragment2'}
        self._attributes = ['Section_parameters', 'FRAGMENT_list']

    def FRAGMENT_add(self, section_parameters=None):
        new_section = _fragment2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FRAGMENT_list.append(new_section)
        return new_section

