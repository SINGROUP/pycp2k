from pycp2k.inputsection import InputSection
from ._becke881 import _becke881
from ._lyp_adiabatic1 import _lyp_adiabatic1
from ._becke88_lr_adiabatic1 import _becke88_lr_adiabatic1
from ._becke88_lr1 import _becke88_lr1
from ._lyp1 import _lyp1
from ._pade1 import _pade1
from ._hcth1 import _hcth1
from ._optx1 import _optx1
from ._libxc1 import _libxc1
from ._ke_libxc1 import _ke_libxc1
from ._cs11 import _cs11
from ._xgga1 import _xgga1
from ._ke_gga1 import _ke_gga1
from ._p86c1 import _p86c1
from ._pw921 import _pw921
from ._pz811 import _pz811
from ._tfw1 import _tfw1
from ._tf1 import _tf1
from ._vwn1 import _vwn1
from ._xalpha1 import _xalpha1
from ._tpss1 import _tpss1
from ._pbe1 import _pbe1
from ._xwpbe1 import _xwpbe1
from ._becke971 import _becke971
from ._becke_roussel1 import _becke_roussel1
from ._lda_hole_t_c_lr1 import _lda_hole_t_c_lr1
from ._pbe_hole_t_c_lr1 import _pbe_hole_t_c_lr1
from ._gv091 import _gv091
from ._beef1 import _beef1


class _xc_functional1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke881()
        self.LYP_ADIABATIC = _lyp_adiabatic1()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic1()
        self.BECKE88_LR = _becke88_lr1()
        self.LYP = _lyp1()
        self.PADE = _pade1()
        self.HCTH_list = []
        self.OPTX = _optx1()
        self.LIBXC = _libxc1()
        self.KE_LIBXC = _ke_libxc1()
        self.CS1 = _cs11()
        self.XGGA_list = []
        self.KE_GGA_list = []
        self.P86C = _p86c1()
        self.PW92_list = []
        self.PZ81_list = []
        self.TFW = _tfw1()
        self.TF = _tf1()
        self.VWN = _vwn1()
        self.XALPHA_list = []
        self.TPSS = _tpss1()
        self.PBE = _pbe1()
        self.XWPBE = _xwpbe1()
        self.BECKE97 = _becke971()
        self.BECKE_ROUSSEL = _becke_roussel1()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr1()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr1()
        self.GV09 = _gv091()
        self.BEEF = _beef1()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'OPTX': 'OPTX', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'BECKE88': 'BECKE88', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'KE_LIBXC': 'KE_LIBXC', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BEEF': 'BEEF', 'TPSS': 'TPSS', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'XWPBE': 'XWPBE', 'PBE': 'PBE', 'GV09': 'GV09', 'BECKE97': 'BECKE97', 'LIBXC': 'LIBXC', 'TF': 'TF', 'P86C': 'P86C', 'CS1': 'CS1', 'VWN': 'VWN', 'PADE': 'PADE', 'TFW': 'TFW'}
        self._repeated_subsections = {'KE_GGA': '_ke_gga1', 'XGGA': '_xgga1', 'PW92': '_pw921', 'XALPHA': '_xalpha1', 'PZ81': '_pz811', 'HCTH': '_hcth1'}
        self._attributes = ['Section_parameters', 'HCTH_list', 'XGGA_list', 'KE_GGA_list', 'PW92_list', 'PZ81_list', 'XALPHA_list']

    def KE_GGA_add(self, section_parameters=None):
        new_section = _ke_gga1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_GGA_list.append(new_section)
        return new_section

    def XGGA_add(self, section_parameters=None):
        new_section = _xgga1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.XGGA_list.append(new_section)
        return new_section

    def PW92_add(self, section_parameters=None):
        new_section = _pw921()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PW92_list.append(new_section)
        return new_section

    def XALPHA_add(self, section_parameters=None):
        new_section = _xalpha1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.XALPHA_list.append(new_section)
        return new_section

    def PZ81_add(self, section_parameters=None):
        new_section = _pz811()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PZ81_list.append(new_section)
        return new_section

    def HCTH_add(self, section_parameters=None):
        new_section = _hcth1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HCTH_list.append(new_section)
        return new_section

