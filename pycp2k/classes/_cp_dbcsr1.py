from pycp2k.inputsection import InputSection


class _cp_dbcsr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_loop = None
        self.Data_type = None
        self.Test_type = None
        self.M = None
        self.N = None
        self.K = None
        self.Transa = None
        self.Transb = None
        self.Bs_m = None
        self.Bs_n = None
        self.Bs_k = None
        self.Atype = None
        self.Btype = None
        self.Ctype = None
        self.Nproc = None
        self.Keepsparse = None
        self.Asparsity = None
        self.Bsparsity = None
        self.Csparsity = None
        self.Alpha = None
        self.Beta = None
        self.Filter_eps = None
        self.Always_checksum = None
        self._name = "CP_DBCSR"
        self._keywords = {'Bs_m': 'BS_M', 'Ctype': 'CTYPE', 'Bs_k': 'BS_K', 'Data_type': 'DATA_TYPE', 'Test_type': 'TEST_TYPE', 'K': 'K', 'Beta': 'BETA', 'Filter_eps': 'FILTER_EPS', 'Alpha': 'ALPHA', 'Atype': 'ATYPE', 'Keepsparse': 'KEEPSPARSE', 'Csparsity': 'CSPARSITY', 'M': 'M', 'Btype': 'BTYPE', 'N_loop': 'N_LOOP', 'Transa': 'TRANSA', 'N': 'N', 'Always_checksum': 'ALWAYS_CHECKSUM', 'Nproc': 'NPROC', 'Bsparsity': 'BSPARSITY', 'Bs_n': 'BS_N', 'Asparsity': 'ASPARSITY', 'Transb': 'TRANSB'}

