from pycp2k.inputsection import InputSection
from ._thermostat_energy7 import _thermostat_energy7
from ._rng_init7 import _rng_init7
from ._s4 import _s4


class _gle4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ndim = None
        self.A_scale = None
        self.A_list = []
        self.C_list = []
        self.THERMOSTAT_ENERGY = _thermostat_energy7()
        self.RNG_INIT = _rng_init7()
        self.S = _s4()
        self._name = "GLE"
        self._keywords = {'A_scale': 'A_SCALE', 'Ndim': 'NDIM'}
        self._repeated_keywords = {'C_list': 'C_LIST', 'A_list': 'A_LIST'}
        self._subsections = {'RNG_INIT': 'RNG_INIT', 'THERMOSTAT_ENERGY': 'THERMOSTAT_ENERGY', 'S': 'S'}

