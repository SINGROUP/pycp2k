from pycp2k.inputsection import InputSection
from ._mode_selective1 import _mode_selective1
from ._print67 import _print67


class _vibrational_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dx = None
        self.Nproc_rep = None
        self.Proc_dist_type = None
        self.Fully_periodic = None
        self.Intensities = None
        self.Thermochemistry = None
        self.Tc_temperature = None
        self.Tc_pressure = None
        self.MODE_SELECTIVE = _mode_selective1()
        self.PRINT = _print67()
        self._name = "VIBRATIONAL_ANALYSIS"
        self._keywords = {'Tc_pressure': 'TC_PRESSURE', 'Proc_dist_type': 'PROC_DIST_TYPE', 'Nproc_rep': 'NPROC_REP', 'Tc_temperature': 'TC_TEMPERATURE', 'Fully_periodic': 'FULLY_PERIODIC', 'Thermochemistry': 'THERMOCHEMISTRY', 'Dx': 'DX', 'Intensities': 'INTENSITIES'}
        self._subsections = {'MODE_SELECTIVE': 'MODE_SELECTIVE', 'PRINT': 'PRINT'}

