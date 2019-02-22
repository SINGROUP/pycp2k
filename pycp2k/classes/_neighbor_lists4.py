from pycp2k.inputsection import InputSection
from ._each221 import _each221


class _neighbor_lists4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Sab_orb = None
        self.Sab_aux_fit = None
        self.Sab_aux_fit_vs_orb = None
        self.Sab_scp = None
        self.Sab_vdw = None
        self.Sab_cn = None
        self.Sac_ae = None
        self.Sac_ppl = None
        self.Sap_ppnl = None
        self.Sap_oce = None
        self.Sab_se = None
        self.Sab_lrc = None
        self.Sab_tbe = None
        self.Sab_core = None
        self.Soo_list = None
        self.Sip_list = None
        self.EACH = _each221()
        self._name = "NEIGHBOR_LISTS"
        self._keywords = {'Sab_cn': 'SAB_CN', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Sap_oce': 'SAP_OCE', 'Sac_ae': 'SAC_AE', 'Sac_ppl': 'SAC_PPL', 'Sab_scp': 'SAB_SCP', 'Soo_list': 'SOO_LIST', 'Sap_ppnl': 'SAP_PPNL', 'Sab_orb': 'SAB_ORB', 'Sab_se': 'SAB_SE', 'Sab_vdw': 'SAB_VDW', 'Sab_lrc': 'SAB_LRC', 'Sab_tbe': 'SAB_TBE', 'Sab_aux_fit': 'SAB_AUX_FIT', 'Filename': 'FILENAME', 'Sip_list': 'SIP_LIST', 'Sab_core': 'SAB_CORE', 'Unit': 'UNIT', 'Sab_aux_fit_vs_orb': 'SAB_AUX_FIT_VS_ORB'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

