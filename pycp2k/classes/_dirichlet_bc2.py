from pycp2k.inputsection import InputSection
from ._aa_planar2 import _aa_planar2
from ._planar2 import _planar2
from ._aa_cylindrical2 import _aa_cylindrical2
from ._aa_cuboidal2 import _aa_cuboidal2


class _dirichlet_bc2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Verbose_output = None
        self.AA_PLANAR_list = []
        self.PLANAR_list = []
        self.AA_CYLINDRICAL_list = []
        self.AA_CUBOIDAL_list = []
        self._name = "DIRICHLET_BC"
        self._keywords = {'Verbose_output': 'VERBOSE_OUTPUT'}
        self._repeated_subsections = {'AA_CYLINDRICAL': '_aa_cylindrical2', 'PLANAR': '_planar2', 'AA_PLANAR': '_aa_planar2', 'AA_CUBOIDAL': '_aa_cuboidal2'}
        self._attributes = ['AA_PLANAR_list', 'PLANAR_list', 'AA_CYLINDRICAL_list', 'AA_CUBOIDAL_list']

    def AA_CYLINDRICAL_add(self, section_parameters=None):
        new_section = _aa_cylindrical2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.AA_CYLINDRICAL_list.append(new_section)
        return new_section

    def PLANAR_add(self, section_parameters=None):
        new_section = _planar2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PLANAR_list.append(new_section)
        return new_section

    def AA_PLANAR_add(self, section_parameters=None):
        new_section = _aa_planar2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.AA_PLANAR_list.append(new_section)
        return new_section

    def AA_CUBOIDAL_add(self, section_parameters=None):
        new_section = _aa_cuboidal2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.AA_CUBOIDAL_list.append(new_section)
        return new_section

