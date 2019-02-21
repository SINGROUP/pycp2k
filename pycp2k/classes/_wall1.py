from pycp2k.inputsection import InputSection
from ._reflective1 import _reflective1
from ._quadratic1 import _quadratic1
from ._quartic1 import _quartic1
from ._gaussian1 import _gaussian1


class _wall1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Position = None
        self.REFLECTIVE = _reflective1()
        self.QUADRATIC = _quadratic1()
        self.QUARTIC = _quartic1()
        self.GAUSSIAN = _gaussian1()
        self._name = "WALL"
        self._keywords = {'Position': 'POSITION', 'Type': 'TYPE'}
        self._subsections = {'REFLECTIVE': 'REFLECTIVE', 'QUARTIC': 'QUARTIC', 'GAUSSIAN': 'GAUSSIAN', 'QUADRATIC': 'QUADRATIC'}

