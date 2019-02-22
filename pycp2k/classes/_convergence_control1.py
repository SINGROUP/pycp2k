from pycp2k.inputsection import InputSection


class _convergence_control1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coarse_grained_width = None
        self.Max_coarse_grained_width = None
        self.Coarse_grained_points = None
        self.Eps_conv = None
        self.K_confidence_limit = None
        self.Sw_confidence_limit = None
        self.Vn_confidence_limit = None
        self._name = "CONVERGENCE_CONTROL"
        self._keywords = {'Sw_confidence_limit': 'SW_CONFIDENCE_LIMIT', 'Coarse_grained_width': 'COARSE_GRAINED_WIDTH', 'Max_coarse_grained_width': 'MAX_COARSE_GRAINED_WIDTH', 'Vn_confidence_limit': 'VN_CONFIDENCE_LIMIT', 'Eps_conv': 'EPS_CONV', 'Coarse_grained_points': 'COARSE_GRAINED_POINTS', 'K_confidence_limit': 'K_CONFIDENCE_LIMIT'}
        self._aliases = {'Cg_points': 'Coarse_grained_points', 'Cg_width': 'Coarse_grained_width', 'Max_cg_width': 'Max_coarse_grained_width'}


    @property
    def Cg_width(self):
        """
        See documentation for Coarse_grained_width
        """
        return self.Coarse_grained_width

    @property
    def Max_cg_width(self):
        """
        See documentation for Max_coarse_grained_width
        """
        return self.Max_coarse_grained_width

    @property
    def Cg_points(self):
        """
        See documentation for Coarse_grained_points
        """
        return self.Coarse_grained_points

    @Cg_width.setter
    def Cg_width(self, value):
        self.Coarse_grained_width = value

    @Max_cg_width.setter
    def Max_cg_width(self, value):
        self.Max_coarse_grained_width = value

    @Cg_points.setter
    def Cg_points(self, value):
        self.Coarse_grained_points = value
