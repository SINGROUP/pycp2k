from pycp2k.inputsection import InputSection
from ._thermostat_fast1 import _thermostat_fast1
from ._thermostat_slow1 import _thermostat_slow1


class _adiabatic_dynamics1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Temp_fast = None
        self.Temp_slow = None
        self.Temp_tol_fast = None
        self.Temp_tol_slow = None
        self.N_resp_fast = None
        self.THERMOSTAT_FAST = _thermostat_fast1()
        self.THERMOSTAT_SLOW = _thermostat_slow1()
        self._name = "ADIABATIC_DYNAMICS"
        self._keywords = {'Temp_tol_fast': 'TEMP_TOL_FAST', 'Temp_fast': 'TEMP_FAST', 'N_resp_fast': 'N_RESP_FAST', 'Temp_tol_slow': 'TEMP_TOL_SLOW', 'Temp_slow': 'TEMP_SLOW'}
        self._subsections = {'THERMOSTAT_FAST': 'THERMOSTAT_FAST', 'THERMOSTAT_SLOW': 'THERMOSTAT_SLOW'}

