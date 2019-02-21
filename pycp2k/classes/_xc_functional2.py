from pycp2k.inputsection import InputSection
from ._becke882 import _becke882
from ._lyp_adiabatic2 import _lyp_adiabatic2
from ._becke88_lr_adiabatic2 import _becke88_lr_adiabatic2
from ._becke88_lr2 import _becke88_lr2
from ._lyp2 import _lyp2
from ._pade2 import _pade2
from ._hcth2 import _hcth2
from ._optx2 import _optx2
from ._libxc2 import _libxc2
from ._ke_libxc2 import _ke_libxc2
from ._cs12 import _cs12
from ._xgga2 import _xgga2
from ._ke_gga2 import _ke_gga2
from ._p86c2 import _p86c2
from ._pw922 import _pw922
from ._pz812 import _pz812
from ._tfw2 import _tfw2
from ._tf2 import _tf2
from ._vwn2 import _vwn2
from ._xalpha2 import _xalpha2
from ._tpss2 import _tpss2
from ._pbe2 import _pbe2
from ._xwpbe2 import _xwpbe2
from ._becke972 import _becke972
from ._becke_roussel2 import _becke_roussel2
from ._lda_hole_t_c_lr2 import _lda_hole_t_c_lr2
from ._pbe_hole_t_c_lr2 import _pbe_hole_t_c_lr2
from ._gv092 import _gv092
from ._beef2 import _beef2


class _xc_functional2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke882()
        self.LYP_ADIABATIC = _lyp_adiabatic2()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic2()
        self.BECKE88_LR = _becke88_lr2()
        self.LYP = _lyp2()
        self.PADE = _pade2()
        self.HCTH_list = []
        self.OPTX = _optx2()
        self.LIBXC = _libxc2()
        self.KE_LIBXC = _ke_libxc2()
        self.CS1 = _cs12()
        self.XGGA_list = []
        self.KE_GGA_list = []
        self.P86C = _p86c2()
        self.PW92_list = []
        self.PZ81_list = []
        self.TFW = _tfw2()
        self.TF = _tf2()
        self.VWN = _vwn2()
        self.XALPHA_list = []
        self.TPSS = _tpss2()
        self.PBE = _pbe2()
        self.XWPBE = _xwpbe2()
        self.BECKE97 = _becke972()
        self.BECKE_ROUSSEL = _becke_roussel2()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr2()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr2()
        self.GV09 = _gv092()
        self.BEEF = _beef2()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'OPTX': 'OPTX', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'BECKE88': 'BECKE88', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'KE_LIBXC': 'KE_LIBXC', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BEEF': 'BEEF', 'TPSS': 'TPSS', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'XWPBE': 'XWPBE', 'PBE': 'PBE', 'GV09': 'GV09', 'BECKE97': 'BECKE97', 'LIBXC': 'LIBXC', 'TF': 'TF', 'P86C': 'P86C', 'CS1': 'CS1', 'VWN': 'VWN', 'PADE': 'PADE', 'TFW': 'TFW'}
        self._repeated_subsections = {'KE_GGA': '_ke_gga2', 'XGGA': '_xgga2', 'PW92': '_pw922', 'XALPHA': '_xalpha2', 'PZ81': '_pz812', 'HCTH': '_hcth2'}
        self._attributes = ['Section_parameters', 'HCTH_list', 'XGGA_list', 'KE_GGA_list', 'PW92_list', 'PZ81_list', 'XALPHA_list']

    def KE_GGA_add(self, section_parameters=None):
        new_section = _ke_gga2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_GGA_list.append(new_section)
        return new_section

    def XGGA_add(self, section_parameters=None):
        new_section = _xgga2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.XGGA_list.append(new_section)
        return new_section

    def PW92_add(self, section_parameters=None):
        new_section = _pw922()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PW92_list.append(new_section)
        return new_section

    def XALPHA_add(self, section_parameters=None):
        new_section = _xalpha2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.XALPHA_list.append(new_section)
        return new_section

    def PZ81_add(self, section_parameters=None):
        new_section = _pz812()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PZ81_list.append(new_section)
        return new_section

    def HCTH_add(self, section_parameters=None):
        new_section = _hcth2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HCTH_list.append(new_section)
        return new_section

