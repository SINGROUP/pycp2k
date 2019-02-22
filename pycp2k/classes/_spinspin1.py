from pycp2k.inputsection import InputSection
from ._print56 import _print56
from ._interpolator11 import _interpolator11


class _spinspin1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Restart_spinspin = None
        self.Issc_on_atom_list = []
        self.Do_fc = None
        self.Do_sd = None
        self.Do_pso = None
        self.Do_dso = None
        self.PRINT = _print56()
        self.INTERPOLATOR = _interpolator11()
        self._name = "SPINSPIN"
        self._keywords = {'Do_dso': 'DO_DSO', 'Restart_spinspin': 'RESTART_SPINSPIN', 'Do_sd': 'DO_SD', 'Do_pso': 'DO_PSO', 'Do_fc': 'DO_FC'}
        self._repeated_keywords = {'Issc_on_atom_list': 'ISSC_ON_ATOM_LIST'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'PRINT': 'PRINT'}
        self._attributes = ['Section_parameters']

