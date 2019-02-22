from pycp2k.inputsection import InputSection
from ._periodic16 import _periodic16
from ._bse5 import _bse5
from ._ic5 import _ic5


class _ri_g0w05(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Corr_mos_occ = None
        self.Corr_mos_virt = None
        self.Scaling = None
        self.Numb_poles = None
        self.Omega_max_fit = None
        self.Stop_crit = None
        self.Print_fit_error = None
        self.Max_iter_fit = None
        self.Check_fit = None
        self.Crossing_search = None
        self.Fermi_level_offset = None
        self.Ev_sc_iter = None
        self.Eps_ev_sc_iter = None
        self.Hf_like_ev_start = None
        self.Ev_sc_gw_remove_neg_virt_energies = None
        self.Print_gw_details = None
        self.Ri_sigma_x = None
        self.Normalize_sigma = None
        self.Neglect_normalization_sigma_x = None
        self.Ri_metric = None
        self.Mix_exchange = None
        self.Fraction_exx = None
        self.Contour_def_start = None
        self.Contour_def_end = None
        self.Contour_def_offset = None
        self.Atoms = None
        self.Atom_range = None
        self.Eps_charge = None
        self.Ic_corr_list = None
        self.Ic_corr_list_beta = None
        self.Periodic = None
        self.Bse = None
        self.Image_charge_model = None
        self.Analytic_continuation = None
        self.Nparam_pade = None
        self.PERIODIC = _periodic16()
        self.BSE = _bse5()
        self.IC = _ic5()
        self._name = "RI_G0W0"
        self._keywords = {'Image_charge_model': 'IMAGE_CHARGE_MODEL', 'Hf_like_ev_start': 'HF_LIKE_EV_START', 'Corr_mos_virt': 'CORR_MOS_VIRT', 'Neglect_normalization_sigma_x': 'NEGLECT_NORMALIZATION_SIGMA_X', 'Eps_ev_sc_iter': 'EPS_EV_SC_ITER', 'Print_fit_error': 'PRINT_FIT_ERROR', 'Analytic_continuation': 'ANALYTIC_CONTINUATION', 'Fermi_level_offset': 'FERMI_LEVEL_OFFSET', 'Contour_def_end': 'CONTOUR_DEF_END', 'Contour_def_start': 'CONTOUR_DEF_START', 'Contour_def_offset': 'CONTOUR_DEF_OFFSET', 'Check_fit': 'CHECK_FIT', 'Atoms': 'ATOMS', 'Normalize_sigma': 'NORMALIZE_SIGMA', 'Ev_sc_iter': 'EV_SC_ITER', 'Ic_corr_list': 'IC_CORR_LIST', 'Mix_exchange': 'MIX_EXCHANGE', 'Periodic': 'PERIODIC', 'Eps_charge': 'EPS_CHARGE', 'Omega_max_fit': 'OMEGA_MAX_FIT', 'Print_gw_details': 'PRINT_GW_DETAILS', 'Corr_mos_occ': 'CORR_MOS_OCC', 'Ri_sigma_x': 'RI_SIGMA_X', 'Fraction_exx': 'FRACTION_EXX', 'Bse': 'BSE', 'Scaling': 'SCALING', 'Ic_corr_list_beta': 'IC_CORR_LIST_BETA', 'Max_iter_fit': 'MAX_ITER_FIT', 'Ev_sc_gw_remove_neg_virt_energies': 'EV_SC_GW_REMOVE_NEG_VIRT_ENERGIES', 'Ri_metric': 'RI_METRIC', 'Nparam_pade': 'NPARAM_PADE', 'Numb_poles': 'NUMB_POLES', 'Atom_range': 'ATOM_RANGE', 'Crossing_search': 'CROSSING_SEARCH', 'Stop_crit': 'STOP_CRIT'}
        self._subsections = {'PERIODIC': 'PERIODIC', 'IC': 'IC', 'BSE': 'BSE'}
        self._aliases = {'Cd_offset': 'Contour_def_offset', 'Remove_neg': 'Ev_sc_gw_remove_neg_virt_energies', 'Ri': 'Ri_metric', 'Ic': 'Image_charge_model', 'A_scaling': 'Scaling', 'Corr_occ': 'Corr_mos_occ', 'Stop_crit_1': 'Stop_crit', 'Cd_start': 'Contour_def_start', 'Alpha': 'Fraction_exx', 'Fit_error': 'Print_fit_error', 'Corr_virt': 'Corr_mos_virt', 'Cd_end': 'Contour_def_end'}


    @property
    def Corr_occ(self):
        """
        See documentation for Corr_mos_occ
        """
        return self.Corr_mos_occ

    @property
    def Corr_virt(self):
        """
        See documentation for Corr_mos_virt
        """
        return self.Corr_mos_virt

    @property
    def A_scaling(self):
        """
        See documentation for Scaling
        """
        return self.Scaling

    @property
    def Stop_crit_1(self):
        """
        See documentation for Stop_crit
        """
        return self.Stop_crit

    @property
    def Fit_error(self):
        """
        See documentation for Print_fit_error
        """
        return self.Print_fit_error

    @property
    def Remove_neg(self):
        """
        See documentation for Ev_sc_gw_remove_neg_virt_energies
        """
        return self.Ev_sc_gw_remove_neg_virt_energies

    @property
    def Ri(self):
        """
        See documentation for Ri_metric
        """
        return self.Ri_metric

    @property
    def Alpha(self):
        """
        See documentation for Fraction_exx
        """
        return self.Fraction_exx

    @property
    def Cd_start(self):
        """
        See documentation for Contour_def_start
        """
        return self.Contour_def_start

    @property
    def Cd_end(self):
        """
        See documentation for Contour_def_end
        """
        return self.Contour_def_end

    @property
    def Cd_offset(self):
        """
        See documentation for Contour_def_offset
        """
        return self.Contour_def_offset

    @property
    def Ic(self):
        """
        See documentation for Image_charge_model
        """
        return self.Image_charge_model

    @Corr_occ.setter
    def Corr_occ(self, value):
        self.Corr_mos_occ = value

    @Corr_virt.setter
    def Corr_virt(self, value):
        self.Corr_mos_virt = value

    @A_scaling.setter
    def A_scaling(self, value):
        self.Scaling = value

    @Stop_crit_1.setter
    def Stop_crit_1(self, value):
        self.Stop_crit = value

    @Fit_error.setter
    def Fit_error(self, value):
        self.Print_fit_error = value

    @Remove_neg.setter
    def Remove_neg(self, value):
        self.Ev_sc_gw_remove_neg_virt_energies = value

    @Ri.setter
    def Ri(self, value):
        self.Ri_metric = value

    @Alpha.setter
    def Alpha(self, value):
        self.Fraction_exx = value

    @Cd_start.setter
    def Cd_start(self, value):
        self.Contour_def_start = value

    @Cd_end.setter
    def Cd_end(self, value):
        self.Contour_def_end = value

    @Cd_offset.setter
    def Cd_offset(self, value):
        self.Contour_def_offset = value

    @Ic.setter
    def Ic(self, value):
        self.Image_charge_model = value
