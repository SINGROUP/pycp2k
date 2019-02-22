from pycp2k.inputsection import InputSection
from ._mol_probabilities1 import _mol_probabilities1
from ._box_probabilities1 import _box_probabilities1


class _move_probabilities1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pmhmc = None
        self.Pmtrans = None
        self.Pmcltrans = None
        self.Pmavbmc = None
        self.Pmtraion = None
        self.Pmswap = None
        self.Pmvolume = None
        self.MOL_PROBABILITIES = _mol_probabilities1()
        self.BOX_PROBABILITIES = _box_probabilities1()
        self._name = "MOVE_PROBABILITIES"
        self._keywords = {'Pmtrans': 'PMTRANS', 'Pmvolume': 'PMVOLUME', 'Pmtraion': 'PMTRAION', 'Pmhmc': 'PMHMC', 'Pmavbmc': 'PMAVBMC', 'Pmswap': 'PMSWAP', 'Pmcltrans': 'PMCLTRANS'}
        self._subsections = {'MOL_PROBABILITIES': 'MOL_PROBABILITIES', 'BOX_PROBABILITIES': 'BOX_PROBABILITIES'}

