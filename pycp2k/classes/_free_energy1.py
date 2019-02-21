from pycp2k.inputsection import InputSection
from ._metadyn1 import _metadyn1
from ._umbrella_integration1 import _umbrella_integration1
from ._alchemical_change1 import _alchemical_change1
from ._free_energy_info1 import _free_energy_info1


class _free_energy1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.METADYN = _metadyn1()
        self.UMBRELLA_INTEGRATION = _umbrella_integration1()
        self.ALCHEMICAL_CHANGE = _alchemical_change1()
        self.FREE_ENERGY_INFO = _free_energy_info1()
        self._name = "FREE_ENERGY"
        self._keywords = {'Method': 'METHOD'}
        self._subsections = {'ALCHEMICAL_CHANGE': 'ALCHEMICAL_CHANGE', 'METADYN': 'METADYN', 'UMBRELLA_INTEGRATION': 'UMBRELLA_INTEGRATION', 'FREE_ENERGY_INFO': 'FREE_ENERGY_INFO'}

