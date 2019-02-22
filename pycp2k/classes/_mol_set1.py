from pycp2k.inputsection import InputSection
from ._molecule1 import _molecule1
from ._merge_molecules1 import _merge_molecules1


class _mol_set1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MOLECULE_list = []
        self.MERGE_MOLECULES = _merge_molecules1()
        self._name = "MOL_SET"
        self._subsections = {'MERGE_MOLECULES': 'MERGE_MOLECULES'}
        self._repeated_subsections = {'MOLECULE': '_molecule1'}
        self._attributes = ['MOLECULE_list']

    def MOLECULE_add(self, section_parameters=None):
        new_section = _molecule1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MOLECULE_list.append(new_section)
        return new_section

