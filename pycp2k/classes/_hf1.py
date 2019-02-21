from pycp2k.inputsection import InputSection
from ._hf_info1 import _hf_info1
from ._periodic1 import _periodic1
from ._screening1 import _screening1
from ._interaction_potential1 import _interaction_potential1
from ._load_balance1 import _load_balance1
from ._memory1 import _memory1


class _hf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info1()
        self.PERIODIC = _periodic1()
        self.SCREENING = _screening1()
        self.INTERACTION_POTENTIAL = _interaction_potential1()
        self.LOAD_BALANCE = _load_balance1()
        self.MEMORY = _memory1()
        self._name = "HF"
        self._keywords = {'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE', 'Fraction': 'FRACTION', 'Pw_hfx': 'PW_HFX'}
        self._subsections = {'SCREENING': 'SCREENING', 'LOAD_BALANCE': 'LOAD_BALANCE', 'PERIODIC': 'PERIODIC', 'MEMORY': 'MEMORY', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'HF_INFO': 'HF_INFO'}

