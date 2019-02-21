from pycp2k.inputsection import InputSection


class _davidson3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Preconditioner = None
        self.Precond_solver = None
        self.Energy_gap = None
        self.New_prec_each = None
        self.First_prec = None
        self.Conv_mos_percent = None
        self.Sparse_mos = None
        self._name = "DAVIDSON"
        self._keywords = {'New_prec_each': 'NEW_PREC_EACH', 'Precond_solver': 'PRECOND_SOLVER', 'Energy_gap': 'ENERGY_GAP', 'Preconditioner': 'PRECONDITIONER', 'Conv_mos_percent': 'CONV_MOS_PERCENT', 'Sparse_mos': 'SPARSE_MOS', 'First_prec': 'FIRST_PREC'}

