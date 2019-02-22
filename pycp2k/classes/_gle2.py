from pycp2k.inputsection import InputSection
from ._thermostat_energy4 import _thermostat_energy4
from ._rng_init4 import _rng_init4
from ._s2 import _s2


class _gle2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ndim = None
        self.A_scale = None
        self.A_list = []
        self.C_list = []
        self.THERMOSTAT_ENERGY = _thermostat_energy4()
        self.RNG_INIT = _rng_init4()
        self.S = _s2()
        self._name = "GLE"
        self._keywords = {'A_scale': 'A_SCALE', 'Ndim': 'NDIM'}
        self._repeated_keywords = {'C_list': 'C_LIST', 'A_list': 'A_LIST'}
        self._subsections = {'RNG_INIT': 'RNG_INIT', 'THERMOSTAT_ENERGY': 'THERMOSTAT_ENERGY', 'S': 'S'}

