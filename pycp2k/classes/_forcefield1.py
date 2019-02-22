from pycp2k.inputsection import InputSection
from ._spline1 import _spline1
from ._nonbonded1 import _nonbonded1
from ._nonbonded141 import _nonbonded141
from ._charge3 import _charge3
from ._charges1 import _charges1
from ._shell2 import _shell2
from ._bond1 import _bond1
from ._bend1 import _bend1
from ._torsion1 import _torsion1
from ._improper1 import _improper1
from ._opbend1 import _opbend1
from ._dipole2 import _dipole2
from ._quadrupole1 import _quadrupole1


class _forcefield1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Parmtype = None
        self.Parm_file_name = None
        self.Vdw_scale14 = None
        self.Ei_scale14 = None
        self.Shift_cutoff = None
        self.Do_nonbonded = None
        self.Ignore_missing_critical_params = None
        self.Multiple_potential = None
        self.Zbl_scattering = None
        self.SPLINE_list = []
        self.NONBONDED = _nonbonded1()
        self.NONBONDED14 = _nonbonded141()
        self.CHARGE_list = []
        self.CHARGES = _charges1()
        self.SHELL_list = []
        self.BOND_list = []
        self.BEND_list = []
        self.TORSION_list = []
        self.IMPROPER_list = []
        self.OPBEND_list = []
        self.DIPOLE_list = []
        self.QUADRUPOLE_list = []
        self._name = "FORCEFIELD"
        self._keywords = {'Parmtype': 'PARMTYPE', 'Ei_scale14': 'EI_SCALE14', 'Zbl_scattering': 'ZBL_SCATTERING', 'Multiple_potential': 'MULTIPLE_POTENTIAL', 'Vdw_scale14': 'VDW_SCALE14', 'Parm_file_name': 'PARM_FILE_NAME', 'Do_nonbonded': 'DO_NONBONDED', 'Shift_cutoff': 'SHIFT_CUTOFF', 'Ignore_missing_critical_params': 'IGNORE_MISSING_CRITICAL_PARAMS'}
        self._subsections = {'NONBONDED14': 'NONBONDED14', 'CHARGES': 'CHARGES', 'NONBONDED': 'NONBONDED'}
        self._repeated_subsections = {'BOND': '_bond1', 'CHARGE': '_charge3', 'IMPROPER': '_improper1', 'BEND': '_bend1', 'TORSION': '_torsion1', 'QUADRUPOLE': '_quadrupole1', 'OPBEND': '_opbend1', 'DIPOLE': '_dipole2', 'SPLINE': '_spline1', 'SHELL': '_shell2'}
        self._attributes = ['SPLINE_list', 'CHARGE_list', 'SHELL_list', 'BOND_list', 'BEND_list', 'TORSION_list', 'IMPROPER_list', 'OPBEND_list', 'DIPOLE_list', 'QUADRUPOLE_list']

    def BOND_add(self, section_parameters=None):
        new_section = _bond1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BOND_list.append(new_section)
        return new_section

    def CHARGE_add(self, section_parameters=None):
        new_section = _charge3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CHARGE_list.append(new_section)
        return new_section

    def IMPROPER_add(self, section_parameters=None):
        new_section = _improper1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.IMPROPER_list.append(new_section)
        return new_section

    def BEND_add(self, section_parameters=None):
        new_section = _bend1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BEND_list.append(new_section)
        return new_section

    def TORSION_add(self, section_parameters=None):
        new_section = _torsion1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.TORSION_list.append(new_section)
        return new_section

    def QUADRUPOLE_add(self, section_parameters=None):
        new_section = _quadrupole1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.QUADRUPOLE_list.append(new_section)
        return new_section

    def OPBEND_add(self, section_parameters=None):
        new_section = _opbend1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.OPBEND_list.append(new_section)
        return new_section

    def DIPOLE_add(self, section_parameters=None):
        new_section = _dipole2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DIPOLE_list.append(new_section)
        return new_section

    def SPLINE_add(self, section_parameters=None):
        new_section = _spline1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.SPLINE_list.append(new_section)
        return new_section

    def SHELL_add(self, section_parameters=None):
        new_section = _shell2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.SHELL_list.append(new_section)
        return new_section

