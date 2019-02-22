from pycp2k.inputsection import InputSection
from ._banner2 import _banner2
from ._program_run_info49 import _program_run_info49
from ._molden_vib1 import _molden_vib1
from ._rotational_info3 import _rotational_info3
from ._cartesian_eigs1 import _cartesian_eigs1
from ._hessian1 import _hessian1


class _print67(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.BANNER = _banner2()
        self.PROGRAM_RUN_INFO = _program_run_info49()
        self.MOLDEN_VIB = _molden_vib1()
        self.ROTATIONAL_INFO = _rotational_info3()
        self.CARTESIAN_EIGS = _cartesian_eigs1()
        self.HESSIAN = _hessian1()
        self._name = "PRINT"
        self._subsections = {'BANNER': 'BANNER', 'HESSIAN': 'HESSIAN', 'CARTESIAN_EIGS': 'CARTESIAN_EIGS', 'MOLDEN_VIB': 'MOLDEN_VIB', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO', 'ROTATIONAL_INFO': 'ROTATIONAL_INFO'}

