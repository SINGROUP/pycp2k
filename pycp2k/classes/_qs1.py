from pycp2k.inputsection import InputSection
from ._distribution1 import _distribution1
from ._dftb1 import _dftb1
from ._se1 import _se1
from ._mulliken_restraint1 import _mulliken_restraint1
from ._ddapc_restraint1 import _ddapc_restraint1
from ._becke_constraint1 import _becke_constraint1
from ._cdft1 import _cdft1
from ._s2_restraint1 import _s2_restraint1
from ._lrigpw1 import _lrigpw1
from ._optimize_lri_basis1 import _optimize_lri_basis1
from ._opt_embed1 import _opt_embed1


class _qs1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_default = None
        self.Eps_core_charge = None
        self.Eps_gvg_rspace = None
        self.Eps_pgf_orb = None
        self.Eps_kg_orb = None
        self.Eps_ppl = None
        self.Eps_ppnl = None
        self.Eps_cpc = None
        self.Eps_rho = None
        self.Eps_rho_rspace = None
        self.Eps_rho_gspace = None
        self.Eps_filter_matrix = None
        self.Epsfit = None
        self.Epsiso = None
        self.Epssvd = None
        self.Epsrho0 = None
        self.Alpha0_hard = None
        self.Force_paw = None
        self.Max_rad_local = None
        self.Ls_scf = None
        self.Almo_scf = None
        self.Transport = None
        self.Kg_method = None
        self.Map_consistent = None
        self.Ref_embed_subsys = None
        self.Cluster_embed_subsys = None
        self.High_level_embed_subsys = None
        self.Lmaxn1 = None
        self.Lmaxn0 = None
        self.Laddn0 = None
        self.Quadrature = None
        self.Pw_grid = None
        self.Pw_grid_layout = None
        self.Pw_grid_blocked = None
        self.Extrapolation = None
        self.Extrapolation_order = None
        self.Method = None
        self.Core_ppl = None
        self.DISTRIBUTION = _distribution1()
        self.DFTB = _dftb1()
        self.SE = _se1()
        self.MULLIKEN_RESTRAINT = _mulliken_restraint1()
        self.DDAPC_RESTRAINT_list = []
        self.BECKE_CONSTRAINT = _becke_constraint1()
        self.CDFT = _cdft1()
        self.S2_RESTRAINT = _s2_restraint1()
        self.LRIGPW = _lrigpw1()
        self.OPTIMIZE_LRI_BASIS = _optimize_lri_basis1()
        self.OPT_EMBED = _opt_embed1()
        self._name = "QS"
        self._keywords = {'Eps_filter_matrix': 'EPS_FILTER_MATRIX', 'Eps_gvg_rspace': 'EPS_GVG_RSPACE', 'Almo_scf': 'ALMO_SCF', 'Lmaxn1': 'LMAXN1', 'Eps_rho_gspace': 'EPS_RHO_GSPACE', 'Lmaxn0': 'LMAXN0', 'Pw_grid': 'PW_GRID', 'Eps_ppl': 'EPS_PPL', 'Laddn0': 'LADDN0', 'Alpha0_hard': 'ALPHA0_HARD', 'Core_ppl': 'CORE_PPL', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'Map_consistent': 'MAP_CONSISTENT', 'Force_paw': 'FORCE_PAW', 'Epsrho0': 'EPSRHO0', 'Eps_kg_orb': 'EPS_KG_ORB', 'Eps_rho': 'EPS_RHO', 'Transport': 'TRANSPORT', 'Eps_rho_rspace': 'EPS_RHO_RSPACE', 'Pw_grid_layout': 'PW_GRID_LAYOUT', 'Kg_method': 'KG_METHOD', 'Epssvd': 'EPSSVD', 'Eps_cpc': 'EPS_CPC', 'High_level_embed_subsys': 'HIGH_LEVEL_EMBED_SUBSYS', 'Epsfit': 'EPSFIT', 'Epsiso': 'EPSISO', 'Eps_core_charge': 'EPS_CORE_CHARGE', 'Ls_scf': 'LS_SCF', 'Method': 'METHOD', 'Cluster_embed_subsys': 'CLUSTER_EMBED_SUBSYS', 'Eps_pgf_orb': 'EPS_PGF_ORB', 'Extrapolation': 'EXTRAPOLATION', 'Ref_embed_subsys': 'REF_EMBED_SUBSYS', 'Quadrature': 'QUADRATURE', 'Pw_grid_blocked': 'PW_GRID_BLOCKED', 'Eps_default': 'EPS_DEFAULT', 'Max_rad_local': 'MAX_RAD_LOCAL', 'Eps_ppnl': 'EPS_PPNL'}
        self._subsections = {'SE': 'SE', 'DISTRIBUTION': 'DISTRIBUTION', 'DFTB': 'DFTB', 'CDFT': 'CDFT', 'MULLIKEN_RESTRAINT': 'MULLIKEN_RESTRAINT', 'BECKE_CONSTRAINT': 'BECKE_CONSTRAINT', 'S2_RESTRAINT': 'S2_RESTRAINT', 'LRIGPW': 'LRIGPW', 'OPT_EMBED': 'OPT_EMBED', 'OPTIMIZE_LRI_BASIS': 'OPTIMIZE_LRI_BASIS'}
        self._repeated_subsections = {'DDAPC_RESTRAINT': '_ddapc_restraint1'}
        self._aliases = {'Lmaxrho1': 'Lmaxn1', 'Interpolation': 'Extrapolation', 'Wf_interpolation': 'Extrapolation', 'Lmaxrho0': 'Lmaxn0', 'Eps_fit': 'Epsfit', 'Eps_vrho0': 'Epsrho0', 'Alpha0_h': 'Alpha0_hard', 'Epsvrho0': 'Epsrho0', 'Eps_iso': 'Epsiso', 'Eps_gvg': 'Eps_gvg_rspace', 'Alpha0': 'Alpha0_hard', 'Eps_svd': 'Epssvd'}
        self._attributes = ['DDAPC_RESTRAINT_list']

    def DDAPC_RESTRAINT_add(self, section_parameters=None):
        new_section = _ddapc_restraint1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DDAPC_RESTRAINT_list.append(new_section)
        return new_section


    @property
    def Eps_gvg(self):
        """
        See documentation for Eps_gvg_rspace
        """
        return self.Eps_gvg_rspace

    @property
    def Eps_fit(self):
        """
        See documentation for Epsfit
        """
        return self.Epsfit

    @property
    def Eps_iso(self):
        """
        See documentation for Epsiso
        """
        return self.Epsiso

    @property
    def Eps_svd(self):
        """
        See documentation for Epssvd
        """
        return self.Epssvd

    @property
    def Epsvrho0(self):
        """
        See documentation for Epsrho0
        """
        return self.Epsrho0

    @property
    def Eps_vrho0(self):
        """
        See documentation for Epsrho0
        """
        return self.Epsrho0

    @property
    def Alpha0_h(self):
        """
        See documentation for Alpha0_hard
        """
        return self.Alpha0_hard

    @property
    def Alpha0(self):
        """
        See documentation for Alpha0_hard
        """
        return self.Alpha0_hard

    @property
    def Lmaxrho1(self):
        """
        See documentation for Lmaxn1
        """
        return self.Lmaxn1

    @property
    def Lmaxrho0(self):
        """
        See documentation for Lmaxn0
        """
        return self.Lmaxn0

    @property
    def Interpolation(self):
        """
        See documentation for Extrapolation
        """
        return self.Extrapolation

    @property
    def Wf_interpolation(self):
        """
        See documentation for Extrapolation
        """
        return self.Extrapolation

    @Eps_gvg.setter
    def Eps_gvg(self, value):
        self.Eps_gvg_rspace = value

    @Eps_fit.setter
    def Eps_fit(self, value):
        self.Epsfit = value

    @Eps_iso.setter
    def Eps_iso(self, value):
        self.Epsiso = value

    @Eps_svd.setter
    def Eps_svd(self, value):
        self.Epssvd = value

    @Epsvrho0.setter
    def Epsvrho0(self, value):
        self.Epsrho0 = value

    @Eps_vrho0.setter
    def Eps_vrho0(self, value):
        self.Epsrho0 = value

    @Alpha0_h.setter
    def Alpha0_h(self, value):
        self.Alpha0_hard = value

    @Alpha0.setter
    def Alpha0(self, value):
        self.Alpha0_hard = value

    @Lmaxrho1.setter
    def Lmaxrho1(self, value):
        self.Lmaxn1 = value

    @Lmaxrho0.setter
    def Lmaxrho0(self, value):
        self.Lmaxn0 = value

    @Interpolation.setter
    def Interpolation(self, value):
        self.Extrapolation = value

    @Wf_interpolation.setter
    def Wf_interpolation(self, value):
        self.Extrapolation = value
