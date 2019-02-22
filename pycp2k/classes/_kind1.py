from pycp2k.inputsection import InputSection
from ._pao_potential1 import _pao_potential1
from ._pao_descriptor1 import _pao_descriptor1
from ._basis2 import _basis2
from ._potential2 import _potential2
from ._kg_potential1 import _kg_potential1
from ._dft_plus_u1 import _dft_plus_u1
from ._bs1 import _bs1


class _kind1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Basis_set = []
        self.Aux_basis_set = None
        self.Ri_aux_basis_set = None
        self.Lri_basis_set = None
        self.Aux_fit_basis_set = None
        self.Elec_conf = None
        self.Core_correction = None
        self.Magnetization = None
        self.Element = None
        self.Mass = None
        self.Potential_file_name = None
        self.Potential_type = None
        self.Potential = None
        self.Kg_potential_file_name = None
        self.Kg_potential = None
        self.Hard_exp_radius = None
        self.Max_rad_local = None
        self.Rho0_exp_radius = None
        self.Lebedev_grid = None
        self.Radial_grid = None
        self.Mm_radius = None
        self.Dftb3_param = None
        self.Lmax_dftb = None
        self.Mao = None
        self.Se_p_orbitals_on_h = None
        self.Gpw_type = None
        self.Ghost = None
        self.Floating_basis_center = None
        self.No_optimize = None
        self.Pao_basis_size = None
        self.PAO_POTENTIAL_list = []
        self.PAO_DESCRIPTOR_list = []
        self.BASIS_list = []
        self.POTENTIAL = _potential2()
        self.KG_POTENTIAL = _kg_potential1()
        self.DFT_PLUS_U = _dft_plus_u1()
        self.BS = _bs1()
        self._name = "KIND"
        self._keywords = {'Lebedev_grid': 'LEBEDEV_GRID', 'Potential': 'POTENTIAL', 'Aux_basis_set': 'AUX_BASIS_SET', 'Potential_file_name': 'POTENTIAL_FILE_NAME', 'Kg_potential': 'KG_POTENTIAL', 'Elec_conf': 'ELEC_CONF', 'Se_p_orbitals_on_h': 'SE_P_ORBITALS_ON_H', 'Mm_radius': 'MM_RADIUS', 'Pao_basis_size': 'PAO_BASIS_SIZE', 'Aux_fit_basis_set': 'AUX_FIT_BASIS_SET', 'Radial_grid': 'RADIAL_GRID', 'Kg_potential_file_name': 'KG_POTENTIAL_FILE_NAME', 'Lmax_dftb': 'LMAX_DFTB', 'Mass': 'MASS', 'Rho0_exp_radius': 'RHO0_EXP_RADIUS', 'Dftb3_param': 'DFTB3_PARAM', 'No_optimize': 'NO_OPTIMIZE', 'Gpw_type': 'GPW_TYPE', 'Floating_basis_center': 'FLOATING_BASIS_CENTER', 'Lri_basis_set': 'LRI_BASIS_SET', 'Core_correction': 'CORE_CORRECTION', 'Ghost': 'GHOST', 'Magnetization': 'MAGNETIZATION', 'Ri_aux_basis_set': 'RI_AUX_BASIS_SET', 'Mao': 'MAO', 'Element': 'ELEMENT', 'Hard_exp_radius': 'HARD_EXP_RADIUS', 'Max_rad_local': 'MAX_RAD_LOCAL', 'Potential_type': 'POTENTIAL_TYPE'}
        self._repeated_keywords = {'Basis_set': 'BASIS_SET'}
        self._subsections = {'KG_POTENTIAL': 'KG_POTENTIAL', 'POTENTIAL': 'POTENTIAL', 'BS': 'BS', 'DFT_PLUS_U': 'DFT_PLUS_U'}
        self._repeated_subsections = {'PAO_DESCRIPTOR': '_pao_descriptor1', 'PAO_POTENTIAL': '_pao_potential1', 'BASIS': '_basis2'}
        self._aliases = {'Auxiliary_basis_set': 'Aux_basis_set', 'Pot': 'Potential', 'Aux_basis': 'Aux_basis_set', 'Auxiliary_fit_basis_set': 'Aux_fit_basis_set', 'Ri_rpa_basis_set': 'Ri_aux_basis_set', 'Aux_fit_basis': 'Aux_fit_basis_set', 'Lri_basis': 'Lri_basis_set', 'Kg_pot': 'Kg_potential', 'Atomic_weight': 'Mass', 'Atomic_mass': 'Mass', 'Weight': 'Mass', 'Ri_aux_basis': 'Ri_aux_basis_set', 'Element_symbol': 'Element', 'Ri_mp2_basis_set': 'Ri_aux_basis_set'}
        self._attributes = ['Section_parameters', 'PAO_POTENTIAL_list', 'PAO_DESCRIPTOR_list', 'BASIS_list']

    def PAO_DESCRIPTOR_add(self, section_parameters=None):
        new_section = _pao_descriptor1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PAO_DESCRIPTOR_list.append(new_section)
        return new_section

    def PAO_POTENTIAL_add(self, section_parameters=None):
        new_section = _pao_potential1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PAO_POTENTIAL_list.append(new_section)
        return new_section

    def BASIS_add(self, section_parameters=None):
        new_section = _basis2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BASIS_list.append(new_section)
        return new_section


    @property
    def Auxiliary_basis_set(self):
        """
        See documentation for Aux_basis_set
        """
        return self.Aux_basis_set

    @property
    def Aux_basis(self):
        """
        See documentation for Aux_basis_set
        """
        return self.Aux_basis_set

    @property
    def Ri_mp2_basis_set(self):
        """
        See documentation for Ri_aux_basis_set
        """
        return self.Ri_aux_basis_set

    @property
    def Ri_rpa_basis_set(self):
        """
        See documentation for Ri_aux_basis_set
        """
        return self.Ri_aux_basis_set

    @property
    def Ri_aux_basis(self):
        """
        See documentation for Ri_aux_basis_set
        """
        return self.Ri_aux_basis_set

    @property
    def Lri_basis(self):
        """
        See documentation for Lri_basis_set
        """
        return self.Lri_basis_set

    @property
    def Auxiliary_fit_basis_set(self):
        """
        See documentation for Aux_fit_basis_set
        """
        return self.Aux_fit_basis_set

    @property
    def Aux_fit_basis(self):
        """
        See documentation for Aux_fit_basis_set
        """
        return self.Aux_fit_basis_set

    @property
    def Element_symbol(self):
        """
        See documentation for Element
        """
        return self.Element

    @property
    def Atomic_mass(self):
        """
        See documentation for Mass
        """
        return self.Mass

    @property
    def Atomic_weight(self):
        """
        See documentation for Mass
        """
        return self.Mass

    @property
    def Weight(self):
        """
        See documentation for Mass
        """
        return self.Mass

    @property
    def Pot(self):
        """
        See documentation for Potential
        """
        return self.Potential

    @property
    def Kg_pot(self):
        """
        See documentation for Kg_potential
        """
        return self.Kg_potential

    @Auxiliary_basis_set.setter
    def Auxiliary_basis_set(self, value):
        self.Aux_basis_set = value

    @Aux_basis.setter
    def Aux_basis(self, value):
        self.Aux_basis_set = value

    @Ri_mp2_basis_set.setter
    def Ri_mp2_basis_set(self, value):
        self.Ri_aux_basis_set = value

    @Ri_rpa_basis_set.setter
    def Ri_rpa_basis_set(self, value):
        self.Ri_aux_basis_set = value

    @Ri_aux_basis.setter
    def Ri_aux_basis(self, value):
        self.Ri_aux_basis_set = value

    @Lri_basis.setter
    def Lri_basis(self, value):
        self.Lri_basis_set = value

    @Auxiliary_fit_basis_set.setter
    def Auxiliary_fit_basis_set(self, value):
        self.Aux_fit_basis_set = value

    @Aux_fit_basis.setter
    def Aux_fit_basis(self, value):
        self.Aux_fit_basis_set = value

    @Element_symbol.setter
    def Element_symbol(self, value):
        self.Element = value

    @Atomic_mass.setter
    def Atomic_mass(self, value):
        self.Mass = value

    @Atomic_weight.setter
    def Atomic_weight(self, value):
        self.Mass = value

    @Weight.setter
    def Weight(self, value):
        self.Mass = value

    @Pot.setter
    def Pot(self, value):
        self.Potential = value

    @Kg_pot.setter
    def Kg_pot(self, value):
        self.Kg_potential = value
