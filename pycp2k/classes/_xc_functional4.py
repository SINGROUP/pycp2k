from pycp2k.inputsection import InputSection
from ._becke884 import _becke884
from ._lyp_adiabatic4 import _lyp_adiabatic4
from ._becke88_lr_adiabatic4 import _becke88_lr_adiabatic4
from ._becke88_lr4 import _becke88_lr4
from ._lyp4 import _lyp4
from ._pade4 import _pade4
from ._hcth4 import _hcth4
from ._optx4 import _optx4
from ._libxc4 import _libxc4
from ._ke_libxc4 import _ke_libxc4
from ._cs14 import _cs14
from ._xgga4 import _xgga4
from ._ke_gga4 import _ke_gga4
from ._p86c4 import _p86c4
from ._pw924 import _pw924
from ._pz814 import _pz814
from ._tfw4 import _tfw4
from ._tf4 import _tf4
from ._vwn4 import _vwn4
from ._xalpha4 import _xalpha4
from ._tpss4 import _tpss4
from ._pbe4 import _pbe4
from ._xwpbe4 import _xwpbe4
from ._becke974 import _becke974
from ._becke_roussel4 import _becke_roussel4
from ._lda_hole_t_c_lr4 import _lda_hole_t_c_lr4
from ._pbe_hole_t_c_lr4 import _pbe_hole_t_c_lr4
from ._gv094 import _gv094
from ._beef4 import _beef4


class _xc_functional4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.BECKE88 = _becke884()
        self.LYP_ADIABATIC = _lyp_adiabatic4()
        self.BECKE88_LR_ADIABATIC = _becke88_lr_adiabatic4()
        self.BECKE88_LR = _becke88_lr4()
        self.LYP = _lyp4()
        self.PADE = _pade4()
        self.HCTH_list = []
        self.OPTX = _optx4()
        self.LIBXC = _libxc4()
        self.KE_LIBXC = _ke_libxc4()
        self.CS1 = _cs14()
        self.XGGA_list = []
        self.KE_GGA_list = []
        self.P86C = _p86c4()
        self.PW92_list = []
        self.PZ81_list = []
        self.TFW = _tfw4()
        self.TF = _tf4()
        self.VWN = _vwn4()
        self.XALPHA_list = []
        self.TPSS = _tpss4()
        self.PBE = _pbe4()
        self.XWPBE = _xwpbe4()
        self.BECKE97 = _becke974()
        self.BECKE_ROUSSEL = _becke_roussel4()
        self.LDA_HOLE_T_C_LR = _lda_hole_t_c_lr4()
        self.PBE_HOLE_T_C_LR = _pbe_hole_t_c_lr4()
        self.GV09 = _gv094()
        self.BEEF = _beef4()
        self._name = "XC_FUNCTIONAL"
        self._subsections = {'BECKE88_LR': 'BECKE88_LR', 'LYP': 'LYP', 'OPTX': 'OPTX', 'BECKE_ROUSSEL': 'BECKE_ROUSSEL', 'BECKE88': 'BECKE88', 'PBE_HOLE_T_C_LR': 'PBE_HOLE_T_C_LR', 'KE_LIBXC': 'KE_LIBXC', 'LYP_ADIABATIC': 'LYP_ADIABATIC', 'BEEF': 'BEEF', 'TPSS': 'TPSS', 'LDA_HOLE_T_C_LR': 'LDA_HOLE_T_C_LR', 'BECKE88_LR_ADIABATIC': 'BECKE88_LR_ADIABATIC', 'XWPBE': 'XWPBE', 'PBE': 'PBE', 'GV09': 'GV09', 'BECKE97': 'BECKE97', 'LIBXC': 'LIBXC', 'TF': 'TF', 'P86C': 'P86C', 'CS1': 'CS1', 'VWN': 'VWN', 'PADE': 'PADE', 'TFW': 'TFW'}
        self._repeated_subsections = {'KE_GGA': '_ke_gga4', 'XGGA': '_xgga4', 'PW92': '_pw924', 'XALPHA': '_xalpha4', 'PZ81': '_pz814', 'HCTH': '_hcth4'}
        self._attributes = ['Section_parameters', 'HCTH_list', 'XGGA_list', 'KE_GGA_list', 'PW92_list', 'PZ81_list', 'XALPHA_list']

    def KE_GGA_add(self, section_parameters=None):
        new_section = _ke_gga4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KE_GGA_list.append(new_section)
        return new_section

    def XGGA_add(self, section_parameters=None):
        new_section = _xgga4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.XGGA_list.append(new_section)
        return new_section

    def PW92_add(self, section_parameters=None):
        new_section = _pw924()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PW92_list.append(new_section)
        return new_section

    def XALPHA_add(self, section_parameters=None):
        new_section = _xalpha4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.XALPHA_list.append(new_section)
        return new_section

    def PZ81_add(self, section_parameters=None):
        new_section = _pz814()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PZ81_list.append(new_section)
        return new_section

    def HCTH_add(self, section_parameters=None):
        new_section = _hcth4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HCTH_list.append(new_section)
        return new_section

