from pycp2k.inputsection import InputSection
from ._outer_scf2 import _outer_scf2
from ._hirshfeld_constraint1 import _hirshfeld_constraint1


class _cdft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type_of_constraint = None
        self.Reuse_precond = None
        self.Precond_freq = None
        self.Max_reuse = None
        self.Purge_history = None
        self.Purge_freq = None
        self.Purge_offset = None
        self.Counter = None
        self.OUTER_SCF = _outer_scf2()
        self.HIRSHFELD_CONSTRAINT = _hirshfeld_constraint1()
        self._name = "CDFT"
        self._keywords = {'Purge_offset': 'PURGE_OFFSET', 'Type_of_constraint': 'TYPE_OF_CONSTRAINT', 'Reuse_precond': 'REUSE_PRECOND', 'Purge_freq': 'PURGE_FREQ', 'Counter': 'COUNTER', 'Purge_history': 'PURGE_HISTORY', 'Precond_freq': 'PRECOND_FREQ', 'Max_reuse': 'MAX_REUSE'}
        self._subsections = {'OUTER_SCF': 'OUTER_SCF', 'HIRSHFELD_CONSTRAINT': 'HIRSHFELD_CONSTRAINT'}

