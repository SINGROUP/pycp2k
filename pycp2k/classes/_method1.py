from pycp2k.inputsection import InputSection
from ._xc5 import _xc5
from ._zmp1 import _zmp1
from ._external_vxc2 import _external_vxc2


class _method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method_type = None
        self.Relativistic = None
        self.XC = _xc5()
        self.ZMP = _zmp1()
        self.EXTERNAL_VXC = _external_vxc2()
        self._name = "METHOD"
        self._keywords = {'Relativistic': 'RELATIVISTIC', 'Method_type': 'METHOD_TYPE'}
        self._subsections = {'ZMP': 'ZMP', 'EXTERNAL_VXC': 'EXTERNAL_VXC', 'XC': 'XC'}

