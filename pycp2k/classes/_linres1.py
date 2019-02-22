from pycp2k.inputsection import InputSection
from ._localize4 import _localize4
from ._current3 import _current3
from ._nmr1 import _nmr1
from ._spinspin1 import _spinspin1
from ._epr1 import _epr1
from ._polar1 import _polar1
from ._print61 import _print61


class _linres1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps = None
        self.Max_iter = None
        self.Restart_every = None
        self.Preconditioner = None
        self.Energy_gap = None
        self.Restart = None
        self.Wfn_restart_file_name = None
        self.LOCALIZE = _localize4()
        self.CURRENT = _current3()
        self.NMR = _nmr1()
        self.SPINSPIN = _spinspin1()
        self.EPR = _epr1()
        self.POLAR = _polar1()
        self.PRINT = _print61()
        self._name = "LINRES"
        self._keywords = {'Eps': 'EPS', 'Energy_gap': 'ENERGY_GAP', 'Preconditioner': 'PRECONDITIONER', 'Restart': 'RESTART', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME', 'Restart_every': 'RESTART_EVERY', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'EPR': 'EPR', 'CURRENT': 'CURRENT', 'PRINT': 'PRINT', 'NMR': 'NMR', 'LOCALIZE': 'LOCALIZE', 'POLAR': 'POLAR', 'SPINSPIN': 'SPINSPIN'}
        self._aliases = {'Restart_file_name': 'Wfn_restart_file_name'}


    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value
