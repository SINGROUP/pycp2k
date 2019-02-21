from pycp2k.inputsection import InputSection
from ._acc1 import _acc1


class _dbcsr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mm_stack_size = None
        self.Mm_driver = None
        self.Avg_elements_images = None
        self.Num_mult_images = None
        self.Use_mpi_allocator = None
        self.Use_mpi_rma = None
        self.Num_layers_3d = None
        self.N_size_mnk_stacks = None
        self.Use_comm_thread = None
        self.Max_elements_per_block = None
        self.Comm_thread_load = None
        self.Multrec_limit = None
        self.ACC = _acc1()
        self._name = "DBCSR"
        self._keywords = {'Mm_stack_size': 'MM_STACK_SIZE', 'Avg_elements_images': 'AVG_ELEMENTS_IMAGES', 'Comm_thread_load': 'COMM_THREAD_LOAD', 'Use_comm_thread': 'USE_COMM_THREAD', 'Num_layers_3d': 'NUM_LAYERS_3D', 'Multrec_limit': 'MULTREC_LIMIT', 'Num_mult_images': 'NUM_MULT_IMAGES', 'Mm_driver': 'MM_DRIVER', 'Use_mpi_allocator': 'USE_MPI_ALLOCATOR', 'N_size_mnk_stacks': 'N_SIZE_MNK_STACKS', 'Max_elements_per_block': 'MAX_ELEMENTS_PER_BLOCK', 'Use_mpi_rma': 'USE_MPI_RMA'}
        self._subsections = {'ACC': 'ACC'}

