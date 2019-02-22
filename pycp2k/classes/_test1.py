from pycp2k.inputsection import InputSection
from ._grid_information1 import _grid_information1
from ._program_run_info2 import _program_run_info2
from ._rs_pw_transfer1 import _rs_pw_transfer1
from ._eigensolver1 import _eigensolver1
from ._pw_transfer1 import _pw_transfer1
from ._cp_fm_gemm1 import _cp_fm_gemm1
from ._cp_dbcsr1 import _cp_dbcsr1
from ._eri_mme_test1 import _eri_mme_test1
from ._shg_integrals_test1 import _shg_integrals_test1


class _test1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Memory = None
        self.Copy = None
        self.Matmul = None
        self.Dgemm = None
        self.Fft = None
        self.Eri = None
        self.Clebsch_gordon = None
        self.Mpi = None
        self.Random_number_generator = None
        self.Minimax = None
        self.Least_sq_ft = None
        self.GRID_INFORMATION = _grid_information1()
        self.PROGRAM_RUN_INFO = _program_run_info2()
        self.RS_PW_TRANSFER = _rs_pw_transfer1()
        self.EIGENSOLVER_list = []
        self.PW_TRANSFER_list = []
        self.CP_FM_GEMM_list = []
        self.CP_DBCSR_list = []
        self.ERI_MME_TEST = _eri_mme_test1()
        self.SHG_INTEGRALS_TEST = _shg_integrals_test1()
        self._name = "TEST"
        self._keywords = {'Fft': 'FFT', 'Dgemm': 'DGEMM', 'Eri': 'ERI', 'Least_sq_ft': 'LEAST_SQ_FT', 'Matmul': 'MATMUL', 'Copy': 'COPY', 'Random_number_generator': 'RANDOM_NUMBER_GENERATOR', 'Minimax': 'MINIMAX', 'Memory': 'MEMORY', 'Mpi': 'MPI', 'Clebsch_gordon': 'CLEBSCH_GORDON'}
        self._subsections = {'GRID_INFORMATION': 'GRID_INFORMATION', 'ERI_MME_TEST': 'ERI_MME_TEST', 'SHG_INTEGRALS_TEST': 'SHG_INTEGRALS_TEST', 'RS_PW_TRANSFER': 'RS_PW_TRANSFER', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}
        self._repeated_subsections = {'CP_FM_GEMM': '_cp_fm_gemm1', 'EIGENSOLVER': '_eigensolver1', 'CP_DBCSR': '_cp_dbcsr1', 'PW_TRANSFER': '_pw_transfer1'}
        self._aliases = {'Rng': 'Random_number_generator', 'Clebsch': 'Clebsch_gordon'}
        self._attributes = ['EIGENSOLVER_list', 'PW_TRANSFER_list', 'CP_FM_GEMM_list', 'CP_DBCSR_list']

    def CP_FM_GEMM_add(self, section_parameters=None):
        new_section = _cp_fm_gemm1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CP_FM_GEMM_list.append(new_section)
        return new_section

    def EIGENSOLVER_add(self, section_parameters=None):
        new_section = _eigensolver1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.EIGENSOLVER_list.append(new_section)
        return new_section

    def CP_DBCSR_add(self, section_parameters=None):
        new_section = _cp_dbcsr1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CP_DBCSR_list.append(new_section)
        return new_section

    def PW_TRANSFER_add(self, section_parameters=None):
        new_section = _pw_transfer1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PW_TRANSFER_list.append(new_section)
        return new_section


    @property
    def Clebsch(self):
        """
        See documentation for Clebsch_gordon
        """
        return self.Clebsch_gordon

    @property
    def Rng(self):
        """
        See documentation for Random_number_generator
        """
        return self.Random_number_generator

    @Clebsch.setter
    def Clebsch(self, value):
        self.Clebsch_gordon = value

    @Rng.setter
    def Rng(self, value):
        self.Random_number_generator = value
