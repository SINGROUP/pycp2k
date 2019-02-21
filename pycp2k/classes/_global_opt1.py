from pycp2k.inputsection import InputSection
from ._progress_trajectory1 import _progress_trajectory1
from ._history2 import _history2
from ._minima_hopping1 import _minima_hopping1
from ._minima_crawling1 import _minima_crawling1


class _global_opt1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.E_target = None
        self.Md_bumps_max = None
        self.Bump_steps_upwards = None
        self.Bump_steps_downwards = None
        self.Fragmentation_threshold = None
        self.PROGRESS_TRAJECTORY = _progress_trajectory1()
        self.HISTORY = _history2()
        self.MINIMA_HOPPING = _minima_hopping1()
        self.MINIMA_CRAWLING = _minima_crawling1()
        self._name = "GLOBAL_OPT"
        self._keywords = {'Fragmentation_threshold': 'FRAGMENTATION_THRESHOLD', 'Method': 'METHOD', 'Bump_steps_downwards': 'BUMP_STEPS_DOWNWARDS', 'Bump_steps_upwards': 'BUMP_STEPS_UPWARDS', 'E_target': 'E_TARGET', 'Md_bumps_max': 'MD_BUMPS_MAX'}
        self._subsections = {'MINIMA_CRAWLING': 'MINIMA_CRAWLING', 'MINIMA_HOPPING': 'MINIMA_HOPPING', 'HISTORY': 'HISTORY', 'PROGRESS_TRAJECTORY': 'PROGRESS_TRAJECTORY'}

