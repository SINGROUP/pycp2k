from pycp2k.inputsection import InputSection
from ._hbonds1 import _hbonds1
from ._g3x31 import _g3x31
from ._g4x61 import _g4x61
from ._virtual_site1 import _virtual_site1
from ._collective1 import _collective1
from ._fixed_atoms1 import _fixed_atoms1
from ._fix_atom_restart1 import _fix_atom_restart1
from ._colvar_restart1 import _colvar_restart1
from ._constraint_info1 import _constraint_info1
from ._lagrange_multipliers1 import _lagrange_multipliers1


class _constraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Shake_tolerance = None
        self.Roll_tolerance = None
        self.Constraint_init = None
        self.HBONDS = _hbonds1()
        self.G3X3_list = []
        self.G4X6_list = []
        self.VIRTUAL_SITE_list = []
        self.COLLECTIVE_list = []
        self.FIXED_ATOMS_list = []
        self.FIX_ATOM_RESTART = _fix_atom_restart1()
        self.COLVAR_RESTART = _colvar_restart1()
        self.CONSTRAINT_INFO = _constraint_info1()
        self.LAGRANGE_MULTIPLIERS = _lagrange_multipliers1()
        self._name = "CONSTRAINT"
        self._keywords = {'Roll_tolerance': 'ROLL_TOLERANCE', 'Constraint_init': 'CONSTRAINT_INIT', 'Shake_tolerance': 'SHAKE_TOLERANCE'}
        self._subsections = {'COLVAR_RESTART': 'COLVAR_RESTART', 'CONSTRAINT_INFO': 'CONSTRAINT_INFO', 'LAGRANGE_MULTIPLIERS': 'LAGRANGE_MULTIPLIERS', 'FIX_ATOM_RESTART': 'FIX_ATOM_RESTART', 'HBONDS': 'HBONDS'}
        self._repeated_subsections = {'G3X3': '_g3x31', 'COLLECTIVE': '_collective1', 'G4X6': '_g4x61', 'VIRTUAL_SITE': '_virtual_site1', 'FIXED_ATOMS': '_fixed_atoms1'}
        self._aliases = {'Roll': 'Roll_tolerance', 'Shake_tol': 'Shake_tolerance', 'Shake': 'Shake_tolerance', 'Roll_tol': 'Roll_tolerance'}
        self._attributes = ['G3X3_list', 'G4X6_list', 'VIRTUAL_SITE_list', 'COLLECTIVE_list', 'FIXED_ATOMS_list']

    def G3X3_add(self, section_parameters=None):
        new_section = _g3x31()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.G3X3_list.append(new_section)
        return new_section

    def COLLECTIVE_add(self, section_parameters=None):
        new_section = _collective1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.COLLECTIVE_list.append(new_section)
        return new_section

    def G4X6_add(self, section_parameters=None):
        new_section = _g4x61()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.G4X6_list.append(new_section)
        return new_section

    def VIRTUAL_SITE_add(self, section_parameters=None):
        new_section = _virtual_site1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.VIRTUAL_SITE_list.append(new_section)
        return new_section

    def FIXED_ATOMS_add(self, section_parameters=None):
        new_section = _fixed_atoms1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FIXED_ATOMS_list.append(new_section)
        return new_section


    @property
    def Shake_tol(self):
        """
        See documentation for Shake_tolerance
        """
        return self.Shake_tolerance

    @property
    def Shake(self):
        """
        See documentation for Shake_tolerance
        """
        return self.Shake_tolerance

    @property
    def Roll_tol(self):
        """
        See documentation for Roll_tolerance
        """
        return self.Roll_tolerance

    @property
    def Roll(self):
        """
        See documentation for Roll_tolerance
        """
        return self.Roll_tolerance

    @Shake_tol.setter
    def Shake_tol(self, value):
        self.Shake_tolerance = value

    @Shake.setter
    def Shake(self, value):
        self.Shake_tolerance = value

    @Roll_tol.setter
    def Roll_tol(self, value):
        self.Roll_tolerance = value

    @Roll.setter
    def Roll(self, value):
        self.Roll_tolerance = value
