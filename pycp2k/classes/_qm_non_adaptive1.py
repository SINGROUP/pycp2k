from pycp2k.inputsection import InputSection
from ._qm_kind1 import _qm_kind1


class _qm_non_adaptive1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.QM_KIND_list = []
        self._name = "QM_NON_ADAPTIVE"
        self._repeated_subsections = {'QM_KIND': '_qm_kind1'}
        self._attributes = ['QM_KIND_list']

    def QM_KIND_add(self, section_parameters=None):
        new_section = _qm_kind1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.QM_KIND_list.append(new_section)
        return new_section

