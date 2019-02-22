from pycp2k.inputsection import InputSection
from ._coulomb1 import _coulomb1
from ._exchange1 import _exchange1
from ._screening3 import _screening3
from ._lr_correction1 import _lr_correction1
from ._neighbor_lists2 import _neighbor_lists2
from ._memory3 import _memory3
from ._print26 import _print26
from ._ga1 import _ga1


class _se1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Orthogonal_basis = None
        self.Sto_ng = None
        self.Analytical_gradients = None
        self.Delta = None
        self.Integral_screening = None
        self.Periodic = None
        self.Force_kdso_d_exchange = None
        self.Dispersion = None
        self.Dispersion_parameter_file = None
        self.Dispersion_radius = None
        self.Coordination_cutoff = None
        self.D3_scaling = None
        self.COULOMB = _coulomb1()
        self.EXCHANGE = _exchange1()
        self.SCREENING = _screening3()
        self.LR_CORRECTION = _lr_correction1()
        self.NEIGHBOR_LISTS = _neighbor_lists2()
        self.MEMORY = _memory3()
        self.PRINT = _print26()
        self.GA = _ga1()
        self._name = "SE"
        self._keywords = {'Sto_ng': 'STO_NG', 'Delta': 'DELTA', 'Analytical_gradients': 'ANALYTICAL_GRADIENTS', 'Coordination_cutoff': 'COORDINATION_CUTOFF', 'Dispersion_radius': 'DISPERSION_RADIUS', 'Orthogonal_basis': 'ORTHOGONAL_BASIS', 'Integral_screening': 'INTEGRAL_SCREENING', 'Force_kdso_d_exchange': 'FORCE_KDSO-D_EXCHANGE', 'Dispersion': 'DISPERSION', 'Periodic': 'PERIODIC', 'Dispersion_parameter_file': 'DISPERSION_PARAMETER_FILE', 'D3_scaling': 'D3_SCALING'}
        self._subsections = {'LR_CORRECTION': 'LR_CORRECTION', 'SCREENING': 'SCREENING', 'GA': 'GA', 'COULOMB': 'COULOMB', 'MEMORY': 'MEMORY', 'EXCHANGE': 'EXCHANGE', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'PRINT': 'PRINT'}

