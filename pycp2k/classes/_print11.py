from pycp2k.inputsection import InputSection
from ._temperature4 import _temperature4
from ._langevin_regions1 import _langevin_regions1


class _print11(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.TEMPERATURE = _temperature4()
        self.LANGEVIN_REGIONS = _langevin_regions1()
        self._name = "PRINT"
        self._subsections = {'LANGEVIN_REGIONS': 'LANGEVIN_REGIONS', 'TEMPERATURE': 'TEMPERATURE'}

