from pycp2k.inputsection import InputSection
from ._each223 import _each223


class _ao_matrices1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Omit_headers = None
        self.Ndigits = None
        self.Core_hamiltonian = None
        self.Density = None
        self.Kinetic_energy = None
        self.Kohn_sham_matrix = None
        self.Matrix_vxc = None
        self.Ortho = None
        self.Overlap = None
        self.Commutator_hr = None
        self.Fermi_contact = None
        self.Pso = None
        self.Efg = None
        self.Potential_energy = None
        self.Oce_hard = None
        self.Oce_soft = None
        self.W_matrix = None
        self.W_matrix_aux_fit = None
        self.Derivatives = None
        self.EACH = _each223()
        self._name = "AO_MATRICES"
        self._keywords = {'Overlap': 'OVERLAP', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Derivatives': 'DERIVATIVES', 'Core_hamiltonian': 'CORE_HAMILTONIAN', 'Oce_hard': 'OCE_HARD', 'Efg': 'EFG', 'Oce_soft': 'OCE_SOFT', 'Matrix_vxc': 'MATRIX_VXC', 'Filename': 'FILENAME', 'Kinetic_energy': 'KINETIC_ENERGY', 'Ndigits': 'NDIGITS', 'W_matrix_aux_fit': 'W_MATRIX_AUX_FIT', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Commutator_hr': 'COMMUTATOR_HR', 'Potential_energy': 'POTENTIAL_ENERGY', 'W_matrix': 'W_MATRIX', 'Kohn_sham_matrix': 'KOHN_SHAM_MATRIX', 'Pso': 'PSO', 'Fermi_contact': 'FERMI_CONTACT', 'Omit_headers': 'OMIT_HEADERS', 'Ortho': 'ORTHO', 'Density': 'DENSITY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

