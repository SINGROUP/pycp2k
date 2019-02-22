from pycp2k.inputsection import InputSection
from ._almo_eda_ct1 import _almo_eda_ct1
from ._almo_cta1 import _almo_cta1


class _print22(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ALMO_EDA_CT = _almo_eda_ct1()
        self.ALMO_CTA = _almo_cta1()
        self._name = "PRINT"
        self._subsections = {'ALMO_CTA': 'ALMO_CTA', 'ALMO_EDA_CT': 'ALMO_EDA_CT'}

