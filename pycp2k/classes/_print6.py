from pycp2k.inputsection import InputSection
from ._thermostat_info1 import _thermostat_info1
from ._temperature1 import _temperature1
from ._energy1 import _energy1


class _print6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.THERMOSTAT_INFO = _thermostat_info1()
        self.TEMPERATURE = _temperature1()
        self.ENERGY = _energy1()
        self._name = "PRINT"
        self._subsections = {'THERMOSTAT_INFO': 'THERMOSTAT_INFO', 'ENERGY': 'ENERGY', 'TEMPERATURE': 'TEMPERATURE'}

