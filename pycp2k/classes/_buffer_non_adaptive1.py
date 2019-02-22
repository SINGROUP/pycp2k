from pycp2k.inputsection import InputSection
from ._qm_kind2 import _qm_kind2
from ._link1 import _link1


class _buffer_non_adaptive1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.QM_KIND_list = []
        self.LINK_list = []
        self._name = "BUFFER_NON_ADAPTIVE"
        self._repeated_subsections = {'QM_KIND': '_qm_kind2', 'LINK': '_link1'}
        self._attributes = ['QM_KIND_list', 'LINK_list']

    def QM_KIND_add(self, section_parameters=None):
        new_section = _qm_kind2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.QM_KIND_list.append(new_section)
        return new_section

    def LINK_add(self, section_parameters=None):
        new_section = _link1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LINK_list.append(new_section)
        return new_section

