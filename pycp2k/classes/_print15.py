from pycp2k.inputsection import InputSection
from ._energy7 import _energy7
from ._action2 import _action2
from ._centroid_pos1 import _centroid_pos1
from ._centroid_vel1 import _centroid_vel1
from ._centroid_gyr1 import _centroid_gyr1
from ._com1 import _com1


class _print15(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Imaginary_time_stride = None
        self.ENERGY = _energy7()
        self.ACTION = _action2()
        self.CENTROID_POS = _centroid_pos1()
        self.CENTROID_VEL = _centroid_vel1()
        self.CENTROID_GYR = _centroid_gyr1()
        self.COM = _com1()
        self._name = "PRINT"
        self._keywords = {'Imaginary_time_stride': 'IMAGINARY_TIME_STRIDE'}
        self._subsections = {'CENTROID_GYR': 'CENTROID_GYR', 'ENERGY': 'ENERGY', 'CENTROID_POS': 'CENTROID_POS', 'CENTROID_VEL': 'CENTROID_VEL', 'ACTION': 'ACTION', 'COM': 'COM'}

