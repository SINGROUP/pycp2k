from pycp2k.inputsection import InputSection


class _string_method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Spline_order = None
        self.Smoothing = None
        self._name = "STRING_METHOD"
        self._keywords = {'Spline_order': 'SPLINE_ORDER', 'Smoothing': 'SMOOTHING'}

