from pycp2k.inputsection import InputSection
from ._hf_info2 import _hf_info2
from ._periodic2 import _periodic2
from ._screening2 import _screening2
from ._interaction_potential2 import _interaction_potential2
from ._load_balance2 import _load_balance2
from ._memory2 import _memory2


class _hf2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info2()
        self.PERIODIC = _periodic2()
        self.SCREENING = _screening2()
        self.INTERACTION_POTENTIAL = _interaction_potential2()
        self.LOAD_BALANCE = _load_balance2()
        self.MEMORY = _memory2()
        self._name = "HF"
        self._keywords = {'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE', 'Fraction': 'FRACTION', 'Pw_hfx': 'PW_HFX'}
        self._subsections = {'SCREENING': 'SCREENING', 'LOAD_BALANCE': 'LOAD_BALANCE', 'PERIODIC': 'PERIODIC', 'MEMORY': 'MEMORY', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'HF_INFO': 'HF_INFO'}

