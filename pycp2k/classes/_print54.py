from pycp2k.inputsection import InputSection
from ._current_cubes1 import _current_cubes1
from ._response_function_cubes1 import _response_function_cubes1


class _print54(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.CURRENT_CUBES = _current_cubes1()
        self.RESPONSE_FUNCTION_CUBES = _response_function_cubes1()
        self._name = "PRINT"
        self._subsections = {'RESPONSE_FUNCTION_CUBES': 'RESPONSE_FUNCTION_CUBES', 'CURRENT_CUBES': 'CURRENT_CUBES'}

