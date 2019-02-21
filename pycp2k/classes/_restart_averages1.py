from pycp2k.inputsection import InputSection


class _restart_averages1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Itimes_start = None
        self.Avecpu = None
        self.Avehugoniot = None
        self.Avetemp_baro = None
        self.Avepot = None
        self.Avekin = None
        self.Avetemp = None
        self.Avekin_qm = None
        self.Avetemp_qm = None
        self.Avevol = None
        self.Avecell_a = None
        self.Avecell_b = None
        self.Avecell_c = None
        self.Avealpha = None
        self.Avebeta = None
        self.Avegamma = None
        self.Ave_econs = None
        self.Ave_press = None
        self.Ave_pxx = None
        self.Ave_pv_vir = None
        self.Ave_pv_tot = None
        self.Ave_pv_kin = None
        self.Ave_pv_cnstr = None
        self.Ave_pv_xc = None
        self.Ave_pv_fock_4c = None
        self.Ave_colvars = None
        self.Ave_mmatrix = None
        self._name = "RESTART_AVERAGES"
        self._keywords = {'Avehugoniot': 'AVEHUGONIOT', 'Ave_pv_kin': 'AVE_PV_KIN', 'Avepot': 'AVEPOT', 'Ave_pv_cnstr': 'AVE_PV_CNSTR', 'Avetemp_baro': 'AVETEMP_BARO', 'Avekin': 'AVEKIN', 'Ave_pv_xc': 'AVE_PV_XC', 'Avebeta': 'AVEBETA', 'Avealpha': 'AVEALPHA', 'Ave_pxx': 'AVE_PXX', 'Ave_press': 'AVE_PRESS', 'Ave_econs': 'AVE_ECONS', 'Ave_pv_fock_4c': 'AVE_PV_FOCK_4C', 'Ave_colvars': 'AVE_COLVARS', 'Ave_mmatrix': 'AVE_MMATRIX', 'Ave_pv_vir': 'AVE_PV_VIR', 'Avecell_c': 'AVECELL_C', 'Avegamma': 'AVEGAMMA', 'Avecell_a': 'AVECELL_A', 'Avekin_qm': 'AVEKIN_QM', 'Avevol': 'AVEVOL', 'Avecell_b': 'AVECELL_B', 'Itimes_start': 'ITIMES_START', 'Avetemp': 'AVETEMP', 'Avecpu': 'AVECPU', 'Avetemp_qm': 'AVETEMP_QM', 'Ave_pv_tot': 'AVE_PV_TOT'}

