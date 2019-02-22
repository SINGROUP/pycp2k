from pycp2k.inputsection import InputSection
from ._thermostat_energy5 import _thermostat_energy5
from ._rng_init5 import _rng_init5


class _csvr3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Timecon = None
        self.THERMOSTAT_ENERGY = _thermostat_energy5()
        self.RNG_INIT = _rng_init5()
        self._name = "CSVR"
        self._keywords = {'Timecon': 'TIMECON'}
        self._subsections = {'RNG_INIT': 'RNG_INIT', 'THERMOSTAT_ENERGY': 'THERMOSTAT_ENERGY'}

