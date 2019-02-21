from pycp2k.inputsection import InputSection
from ._rng_init8 import _rng_init8


class _pile1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Tau = None
        self.Lambda = None
        self.RNG_INIT = _rng_init8()
        self._name = "PILE"
        self._keywords = {'Tau': 'TAU', 'Lambda': 'LAMBDA'}
        self._subsections = {'RNG_INIT': 'RNG_INIT'}

