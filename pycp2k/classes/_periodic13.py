from pycp2k.inputsection import InputSection


class _periodic13(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Kpoints = []
        self.Num_kp_grids = None
        self.Eps_kpoint = None
        self.Mo_coeff_gamma = None
        self.Average_degenerate_levels = None
        self.Eps_eigenval = None
        self.Extrapolate_kpoints = None
        self.Do_aux_bas_gw = None
        self.Fraction_aux_mos = None
        self.Contour_def_end = None
        self.Num_omega_points = None
        self._name = "PERIODIC"
        self._keywords = {'Eps_eigenval': 'EPS_EIGENVAL', 'Mo_coeff_gamma': 'MO_COEFF_GAMMA', 'Num_kp_grids': 'NUM_KP_GRIDS', 'Extrapolate_kpoints': 'EXTRAPOLATE_KPOINTS', 'Average_degenerate_levels': 'AVERAGE_DEGENERATE_LEVELS', 'Fraction_aux_mos': 'FRACTION_AUX_MOS', 'Eps_kpoint': 'EPS_KPOINT', 'Num_omega_points': 'NUM_OMEGA_POINTS', 'Contour_def_end': 'CONTOUR_DEF_END', 'Do_aux_bas_gw': 'DO_AUX_BAS_GW'}
        self._repeated_keywords = {'Kpoints': 'KPOINTS'}
        self._aliases = {'Adl': 'Average_degenerate_levels', 'Extrapolate': 'Extrapolate_kpoints', 'Cd_end': 'Contour_def_end'}


    @property
    def Adl(self):
        """
        See documentation for Average_degenerate_levels
        """
        return self.Average_degenerate_levels

    @property
    def Extrapolate(self):
        """
        See documentation for Extrapolate_kpoints
        """
        return self.Extrapolate_kpoints

    @property
    def Cd_end(self):
        """
        See documentation for Contour_def_end
        """
        return self.Contour_def_end

    @Adl.setter
    def Adl(self, value):
        self.Average_degenerate_levels = value

    @Extrapolate.setter
    def Extrapolate(self, value):
        self.Extrapolate_kpoints = value

    @Cd_end.setter
    def Cd_end(self, value):
        self.Contour_def_end = value
