from pycp2k.inputsection import InputSection
from ._hf6 import _hf6
from ._ri_g0w03 import _ri_g0w03
from ._im_time3 import _im_time3
from ._ri_axk3 import _ri_axk3


class _ri_rpa3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Quadrature_points = None
        self.Size_freq_integ_group = None
        self.Mm_style = None
        self.Minimax_quadrature = None
        self.Ri_g0w0 = None
        self.Ri_axk = None
        self.Admm = None
        self.Im_time = None
        self.HF_list = []
        self.RI_G0W0 = _ri_g0w03()
        self.IM_TIME = _im_time3()
        self.RI_AXK = _ri_axk3()
        self._name = "RI_RPA"
        self._keywords = {'Admm': 'ADMM', 'Mm_style': 'MM_STYLE', 'Im_time': 'IM_TIME', 'Ri_g0w0': 'RI_G0W0', 'Minimax_quadrature': 'MINIMAX_QUADRATURE', 'Ri_axk': 'RI_AXK', 'Quadrature_points': 'QUADRATURE_POINTS', 'Size_freq_integ_group': 'SIZE_FREQ_INTEG_GROUP'}
        self._subsections = {'RI_AXK': 'RI_AXK', 'IM_TIME': 'IM_TIME', 'RI_G0W0': 'RI_G0W0'}
        self._repeated_subsections = {'HF': '_hf6'}
        self._aliases = {'Axk': 'Ri_axk', 'Imag_time': 'Im_time', 'Rpa_group_size': 'Size_freq_integ_group', 'Minimax': 'Minimax_quadrature', 'Gw': 'Ri_g0w0', 'Rpa_num_quad_points': 'Quadrature_points'}
        self._attributes = ['HF_list']

    def HF_add(self, section_parameters=None):
        new_section = _hf6()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HF_list.append(new_section)
        return new_section


    @property
    def Rpa_num_quad_points(self):
        """
        See documentation for Quadrature_points
        """
        return self.Quadrature_points

    @property
    def Rpa_group_size(self):
        """
        See documentation for Size_freq_integ_group
        """
        return self.Size_freq_integ_group

    @property
    def Minimax(self):
        """
        See documentation for Minimax_quadrature
        """
        return self.Minimax_quadrature

    @property
    def Gw(self):
        """
        See documentation for Ri_g0w0
        """
        return self.Ri_g0w0

    @property
    def Axk(self):
        """
        See documentation for Ri_axk
        """
        return self.Ri_axk

    @property
    def Imag_time(self):
        """
        See documentation for Im_time
        """
        return self.Im_time

    @Rpa_num_quad_points.setter
    def Rpa_num_quad_points(self, value):
        self.Quadrature_points = value

    @Rpa_group_size.setter
    def Rpa_group_size(self, value):
        self.Size_freq_integ_group = value

    @Minimax.setter
    def Minimax(self, value):
        self.Minimax_quadrature = value

    @Gw.setter
    def Gw(self, value):
        self.Ri_g0w0 = value

    @Axk.setter
    def Axk(self, value):
        self.Ri_axk = value

    @Imag_time.setter
    def Imag_time(self, value):
        self.Im_time = value
