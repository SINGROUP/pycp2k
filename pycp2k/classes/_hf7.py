from pycp2k.inputsection import InputSection
from ._hf_info7 import _hf_info7
from ._periodic11 import _periodic11
from ._screening8 import _screening8
from ._interaction_potential10 import _interaction_potential10
from ._load_balance7 import _load_balance7
from ._memory8 import _memory8


class _hf7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info7()
        self.PERIODIC = _periodic11()
        self.SCREENING = _screening8()
        self.INTERACTION_POTENTIAL = _interaction_potential10()
        self.LOAD_BALANCE = _load_balance7()
        self.MEMORY = _memory8()
        self._name = "HF"
        self._keywords = {'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE', 'Fraction': 'FRACTION', 'Pw_hfx': 'PW_HFX'}
        self._subsections = {'SCREENING': 'SCREENING', 'LOAD_BALANCE': 'LOAD_BALANCE', 'PERIODIC': 'PERIODIC', 'MEMORY': 'MEMORY', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'HF_INFO': 'HF_INFO'}

