from pycp2k.inputsection import InputSection
from ._move_mm_charge3 import _move_mm_charge3
from ._add_mm_charge3 import _add_mm_charge3


class _link3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Qm_index = None
        self.Qm_kind = None
        self.Mm_index = None
        self.Radius = None
        self.Corr_radius = None
        self.Link_type = None
        self.Alpha_imomm = None
        self.Qmmm_scale_factor = None
        self.Fist_scale_factor = None
        self.MOVE_MM_CHARGE_list = []
        self.ADD_MM_CHARGE_list = []
        self._name = "LINK"
        self._keywords = {'Corr_radius': 'CORR_RADIUS', 'Mm_index': 'MM_INDEX', 'Qm_index': 'QM_INDEX', 'Alpha_imomm': 'ALPHA_IMOMM', 'Link_type': 'LINK_TYPE', 'Qmmm_scale_factor': 'QMMM_SCALE_FACTOR', 'Radius': 'RADIUS', 'Qm_kind': 'QM_KIND', 'Fist_scale_factor': 'FIST_SCALE_FACTOR'}
        self._repeated_subsections = {'ADD_MM_CHARGE': '_add_mm_charge3', 'MOVE_MM_CHARGE': '_move_mm_charge3'}
        self._aliases = {'Qm': 'Qm_index', 'Qmmm_charge_scale': 'Qmmm_scale_factor', 'Qmmm_charge_factor': 'Qmmm_scale_factor', 'Fist_charge_scale': 'Fist_scale_factor', 'Link': 'Link_type', 'Type': 'Link_type', 'Qmmm_scale_charge': 'Qmmm_scale_factor', 'Ltype': 'Link_type', 'Fist_scale_charge': 'Fist_scale_factor', 'Mm': 'Mm_index', 'Alpha': 'Alpha_imomm', 'Fist_charge_factor': 'Fist_scale_factor'}
        self._attributes = ['MOVE_MM_CHARGE_list', 'ADD_MM_CHARGE_list']

    def ADD_MM_CHARGE_add(self, section_parameters=None):
        new_section = _add_mm_charge3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.ADD_MM_CHARGE_list.append(new_section)
        return new_section

    def MOVE_MM_CHARGE_add(self, section_parameters=None):
        new_section = _move_mm_charge3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MOVE_MM_CHARGE_list.append(new_section)
        return new_section


    @property
    def Qm(self):
        """
        See documentation for Qm_index
        """
        return self.Qm_index

    @property
    def Mm(self):
        """
        See documentation for Mm_index
        """
        return self.Mm_index

    @property
    def Link(self):
        """
        See documentation for Link_type
        """
        return self.Link_type

    @property
    def Type(self):
        """
        See documentation for Link_type
        """
        return self.Link_type

    @property
    def Ltype(self):
        """
        See documentation for Link_type
        """
        return self.Link_type

    @property
    def Alpha(self):
        """
        See documentation for Alpha_imomm
        """
        return self.Alpha_imomm

    @property
    def Qmmm_charge_scale(self):
        """
        See documentation for Qmmm_scale_factor
        """
        return self.Qmmm_scale_factor

    @property
    def Qmmm_charge_factor(self):
        """
        See documentation for Qmmm_scale_factor
        """
        return self.Qmmm_scale_factor

    @property
    def Qmmm_scale_charge(self):
        """
        See documentation for Qmmm_scale_factor
        """
        return self.Qmmm_scale_factor

    @property
    def Fist_charge_scale(self):
        """
        See documentation for Fist_scale_factor
        """
        return self.Fist_scale_factor

    @property
    def Fist_charge_factor(self):
        """
        See documentation for Fist_scale_factor
        """
        return self.Fist_scale_factor

    @property
    def Fist_scale_charge(self):
        """
        See documentation for Fist_scale_factor
        """
        return self.Fist_scale_factor

    @Qm.setter
    def Qm(self, value):
        self.Qm_index = value

    @Mm.setter
    def Mm(self, value):
        self.Mm_index = value

    @Link.setter
    def Link(self, value):
        self.Link_type = value

    @Type.setter
    def Type(self, value):
        self.Link_type = value

    @Ltype.setter
    def Ltype(self, value):
        self.Link_type = value

    @Alpha.setter
    def Alpha(self, value):
        self.Alpha_imomm = value

    @Qmmm_charge_scale.setter
    def Qmmm_charge_scale(self, value):
        self.Qmmm_scale_factor = value

    @Qmmm_charge_factor.setter
    def Qmmm_charge_factor(self, value):
        self.Qmmm_scale_factor = value

    @Qmmm_scale_charge.setter
    def Qmmm_scale_charge(self, value):
        self.Qmmm_scale_factor = value

    @Fist_charge_scale.setter
    def Fist_charge_scale(self, value):
        self.Fist_scale_factor = value

    @Fist_charge_factor.setter
    def Fist_charge_factor(self, value):
        self.Fist_scale_factor = value

    @Fist_scale_charge.setter
    def Fist_scale_charge(self, value):
        self.Fist_scale_factor = value
