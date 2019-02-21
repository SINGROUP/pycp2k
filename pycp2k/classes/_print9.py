from pycp2k.inputsection import InputSection
from ._thermostat_info3 import _thermostat_info3
from ._temperature3 import _temperature3
from ._energy4 import _energy4


class _print9(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.THERMOSTAT_INFO = _thermostat_info3()
        self.TEMPERATURE = _temperature3()
        self.ENERGY = _energy4()
        self._name = "PRINT"
        self._subsections = {'THERMOSTAT_INFO': 'THERMOSTAT_INFO', 'ENERGY': 'ENERGY', 'TEMPERATURE': 'TEMPERATURE'}

