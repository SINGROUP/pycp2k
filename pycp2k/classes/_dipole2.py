from pycp2k.inputsection import InputSection
from ._damping1 import _damping1


class _dipole2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom = None
        self.Apol = None
        self.DAMPING_list = []
        self._name = "DIPOLE"
        self._keywords = {'Atom': 'ATOM', 'Apol': 'APOL'}
        self._repeated_subsections = {'DAMPING': '_damping1'}
        self._attributes = ['DAMPING_list']

    def DAMPING_add(self, section_parameters=None):
        new_section = _damping1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DAMPING_list.append(new_section)
        return new_section

