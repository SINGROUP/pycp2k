from pycp2k.inputsection import InputSection
from ._hf_info10 import _hf_info10
from ._periodic15 import _periodic15
from ._screening11 import _screening11
from ._interaction_potential14 import _interaction_potential14
from ._load_balance10 import _load_balance10
from ._memory11 import _memory11


class _hf10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info10()
        self.PERIODIC = _periodic15()
        self.SCREENING = _screening11()
        self.INTERACTION_POTENTIAL = _interaction_potential14()
        self.LOAD_BALANCE = _load_balance10()
        self.MEMORY = _memory11()
        self._name = "HF"
        self._keywords = {'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE', 'Fraction': 'FRACTION', 'Pw_hfx': 'PW_HFX'}
        self._subsections = {'SCREENING': 'SCREENING', 'LOAD_BALANCE': 'LOAD_BALANCE', 'PERIODIC': 'PERIODIC', 'MEMORY': 'MEMORY', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'HF_INFO': 'HF_INFO'}

