from pycp2k.inputsection import InputSection
from ._print_averages1 import _print_averages1
from ._restart_averages1 import _restart_averages1


class _averages1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Acquisition_start_time = None
        self.Average_colvar = None
        self.PRINT_AVERAGES = _print_averages1()
        self.RESTART_AVERAGES = _restart_averages1()
        self._name = "AVERAGES"
        self._keywords = {'Acquisition_start_time': 'ACQUISITION_START_TIME', 'Average_colvar': 'AVERAGE_COLVAR'}
        self._subsections = {'PRINT_AVERAGES': 'PRINT_AVERAGES', 'RESTART_AVERAGES': 'RESTART_AVERAGES'}
        self._attributes = ['Section_parameters']

