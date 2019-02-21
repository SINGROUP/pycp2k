from pycp2k.inputsection import InputSection
from ._nonbonded2 import _nonbonded2
from ._nonbonded142 import _nonbonded142


class _forcefield2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Multiple_potential = None
        self.NONBONDED_list = []
        self.NONBONDED14 = _nonbonded142()
        self._name = "FORCEFIELD"
        self._keywords = {'Multiple_potential': 'MULTIPLE_POTENTIAL'}
        self._subsections = {'NONBONDED14': 'NONBONDED14'}
        self._repeated_subsections = {'NONBONDED': '_nonbonded2'}
        self._attributes = ['NONBONDED_list']

    def NONBONDED_add(self, section_parameters=None):
        new_section = _nonbonded2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.NONBONDED_list.append(new_section)
        return new_section

