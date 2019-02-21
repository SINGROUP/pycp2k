from pycp2k.inputsection import InputSection
from ._program_run_info20 import _program_run_info20


class _density_fitting1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Num_gauss = None
        self.Pfactor = None
        self.Min_radius = None
        self.Radii = None
        self.Gcut = None
        self.PROGRAM_RUN_INFO = _program_run_info20()
        self._name = "DENSITY_FITTING"
        self._keywords = {'Num_gauss': 'NUM_GAUSS', 'Min_radius': 'MIN_RADIUS', 'Radii': 'RADII', 'Gcut': 'GCUT', 'Pfactor': 'PFACTOR'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

