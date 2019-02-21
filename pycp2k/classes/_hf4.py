from pycp2k.inputsection import InputSection
from ._hf_info4 import _hf_info4
from ._periodic5 import _periodic5
from ._screening5 import _screening5
from ._interaction_potential5 import _interaction_potential5
from ._load_balance4 import _load_balance4
from ._memory5 import _memory5


class _hf4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Fraction = None
        self.Treat_lsd_in_core = None
        self.Pw_hfx = None
        self.Pw_hfx_blocksize = None
        self.HF_INFO = _hf_info4()
        self.PERIODIC = _periodic5()
        self.SCREENING = _screening5()
        self.INTERACTION_POTENTIAL = _interaction_potential5()
        self.LOAD_BALANCE = _load_balance4()
        self.MEMORY = _memory5()
        self._name = "HF"
        self._keywords = {'Treat_lsd_in_core': 'TREAT_LSD_IN_CORE', 'Pw_hfx_blocksize': 'PW_HFX_BLOCKSIZE', 'Fraction': 'FRACTION', 'Pw_hfx': 'PW_HFX'}
        self._subsections = {'SCREENING': 'SCREENING', 'LOAD_BALANCE': 'LOAD_BALANCE', 'PERIODIC': 'PERIODIC', 'MEMORY': 'MEMORY', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'HF_INFO': 'HF_INFO'}

