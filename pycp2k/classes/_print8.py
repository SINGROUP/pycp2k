from pycp2k.inputsection import InputSection
from ._thermostat_info2 import _thermostat_info2
from ._temperature2 import _temperature2
from ._energy3 import _energy3


class _print8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.THERMOSTAT_INFO = _thermostat_info2()
        self.TEMPERATURE = _temperature2()
        self.ENERGY = _energy3()
        self._name = "PRINT"
        self._subsections = {'THERMOSTAT_INFO': 'THERMOSTAT_INFO', 'ENERGY': 'ENERGY', 'TEMPERATURE': 'TEMPERATURE'}

