from pycp2k.inputsection import InputSection
from ._link2 import _link2


class _buffer_links1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.LINK_list = []
        self._name = "BUFFER_LINKS"
        self._repeated_subsections = {'LINK': '_link2'}
        self._attributes = ['LINK_list']

    def LINK_add(self, section_parameters=None):
        new_section = _link2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LINK_list.append(new_section)
        return new_section

