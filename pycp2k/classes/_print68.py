from pycp2k.inputsection import InputSection
from ._program_banner4 import _program_banner4
from ._method_info1 import _method_info1
from ._basis_set1 import _basis_set1
from ._potential3 import _potential3
from ._fit_density1 import _fit_density1
from ._fit_kgpot1 import _fit_kgpot1
from ._response_basis1 import _response_basis1
from ._geometrical_response_basis1 import _geometrical_response_basis1
from ._scf_info1 import _scf_info1
from ._orbitals1 import _orbitals1
from ._analyze_basis1 import _analyze_basis1
from ._fit_pseudo1 import _fit_pseudo1
from ._fit_basis1 import _fit_basis1
from ._upf_file1 import _upf_file1
from ._separable_gaussian_pseudo1 import _separable_gaussian_pseudo1
from ._admm1 import _admm1


class _print68(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_BANNER = _program_banner4()
        self.METHOD_INFO = _method_info1()
        self.BASIS_SET = _basis_set1()
        self.POTENTIAL = _potential3()
        self.FIT_DENSITY = _fit_density1()
        self.FIT_KGPOT = _fit_kgpot1()
        self.RESPONSE_BASIS = _response_basis1()
        self.GEOMETRICAL_RESPONSE_BASIS = _geometrical_response_basis1()
        self.SCF_INFO = _scf_info1()
        self.ORBITALS = _orbitals1()
        self.ANALYZE_BASIS = _analyze_basis1()
        self.FIT_PSEUDO = _fit_pseudo1()
        self.FIT_BASIS = _fit_basis1()
        self.UPF_FILE = _upf_file1()
        self.SEPARABLE_GAUSSIAN_PSEUDO = _separable_gaussian_pseudo1()
        self.ADMM = _admm1()
        self._name = "PRINT"
        self._subsections = {'ORBITALS': 'ORBITALS', 'FIT_PSEUDO': 'FIT_PSEUDO', 'FIT_BASIS': 'FIT_BASIS', 'SCF_INFO': 'SCF_INFO', 'RESPONSE_BASIS': 'RESPONSE_BASIS', 'BASIS_SET': 'BASIS_SET', 'GEOMETRICAL_RESPONSE_BASIS': 'GEOMETRICAL_RESPONSE_BASIS', 'SEPARABLE_GAUSSIAN_PSEUDO': 'SEPARABLE_GAUSSIAN_PSEUDO', 'ADMM': 'ADMM', 'FIT_DENSITY': 'FIT_DENSITY', 'METHOD_INFO': 'METHOD_INFO', 'PROGRAM_BANNER': 'PROGRAM_BANNER', 'UPF_FILE': 'UPF_FILE', 'POTENTIAL': 'POTENTIAL', 'FIT_KGPOT': 'FIT_KGPOT', 'ANALYZE_BASIS': 'ANALYZE_BASIS'}

