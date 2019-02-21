from pycp2k.inputsection import InputSection


class _cp_fm_gemm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_loop = None
        self.K = None
        self.M = None
        self.N = None
        self.Nrow_block = None
        self.Ncol_block = None
        self.Row_major = None
        self.Force_blocksize = None
        self.Grid_2d = None
        self.Transa = None
        self.Transb = None
        self._name = "CP_FM_GEMM"
        self._keywords = {'Transb': 'TRANSB', 'M': 'M', 'N_loop': 'N_LOOP', 'Grid_2d': 'GRID_2D', 'Transa': 'TRANSA', 'Ncol_block': 'NCOL_BLOCK', 'Force_blocksize': 'FORCE_BLOCKSIZE', 'N': 'N', 'Nrow_block': 'NROW_BLOCK', 'K': 'K', 'Row_major': 'ROW_MAJOR'}

