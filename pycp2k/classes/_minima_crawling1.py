from pycp2k.inputsection import InputSection
from ._minima_trajectory1 import _minima_trajectory1


class _minima_crawling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Tempstep_base = None
        self.Tempstep_max = None
        self.Tempdist_update_width = None
        self.Tempdist_update_height = None
        self.Temperature_init = None
        self.Tempdist_init_width = None
        self.Worker_per_minima = None
        self.Escape_history_length = None
        self.MINIMA_TRAJECTORY = _minima_trajectory1()
        self._name = "MINIMA_CRAWLING"
        self._keywords = {'Escape_history_length': 'ESCAPE_HISTORY_LENGTH', 'Tempdist_init_width': 'TEMPDIST_INIT_WIDTH', 'Tempdist_update_width': 'TEMPDIST_UPDATE_WIDTH', 'Tempstep_base': 'TEMPSTEP_BASE', 'Tempstep_max': 'TEMPSTEP_MAX', 'Temperature_init': 'TEMPERATURE_INIT', 'Worker_per_minima': 'WORKER_PER_MINIMA', 'Tempdist_update_height': 'TEMPDIST_UPDATE_HEIGHT'}
        self._subsections = {'MINIMA_TRAJECTORY': 'MINIMA_TRAJECTORY'}

