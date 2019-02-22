from pycp2k.inputsection import InputSection
from ._contact1 import _contact1
from ._beyn1 import _beyn1
from ._pexsi2 import _pexsi2
from ._print31 import _print31


class _transport1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Transport_method = None
        self.Qt_formalism = None
        self.Num_pole = None
        self.N_kpoints = None
        self.Num_interval = None
        self.Tasks_per_energy_point = None
        self.Tasks_per_pole = None
        self.Gpus_per_point = None
        self.Colzero_threshold = None
        self.Eps_limit = None
        self.Eps_limit_cc = None
        self.Eps_decay = None
        self.Eps_singularity_curvatures = None
        self.Eps_mu = None
        self.Eps_eigval_degen = None
        self.Eps_fermi = None
        self.Energy_interval = None
        self.Min_interval = None
        self.Temperature = None
        self.Csr_screening = None
        self.Linear_solver = None
        self.Matrix_inversion_method = None
        self.Injection_method = None
        self.Cutout = None
        self.Real_axis_integration_method = None
        self.N_points_inv = None
        self.Obc_equilibrium = None
        self.Contact_filling = None
        self.Density_mixing = None
        self.CONTACT_list = []
        self.BEYN = _beyn1()
        self.PEXSI = _pexsi2()
        self.PRINT = _print31()
        self._name = "TRANSPORT"
        self._keywords = {'Min_interval': 'MIN_INTERVAL', 'Num_pole': 'NUM_POLE', 'Matrix_inversion_method': 'MATRIX_INVERSION_METHOD', 'Density_mixing': 'DENSITY_MIXING', 'Tasks_per_energy_point': 'TASKS_PER_ENERGY_POINT', 'Temperature': 'TEMPERATURE', 'Gpus_per_point': 'GPUS_PER_POINT', 'Eps_eigval_degen': 'EPS_EIGVAL_DEGEN', 'Csr_screening': 'CSR_SCREENING', 'Linear_solver': 'LINEAR_SOLVER', 'Contact_filling': 'CONTACT_FILLING', 'Num_interval': 'NUM_INTERVAL', 'Eps_singularity_curvatures': 'EPS_SINGULARITY_CURVATURES', 'Energy_interval': 'ENERGY_INTERVAL', 'N_kpoints': 'N_KPOINTS', 'Tasks_per_pole': 'TASKS_PER_POLE', 'Cutout': 'CUTOUT', 'Qt_formalism': 'QT_FORMALISM', 'Injection_method': 'INJECTION_METHOD', 'Real_axis_integration_method': 'REAL_AXIS_INTEGRATION_METHOD', 'Obc_equilibrium': 'OBC_EQUILIBRIUM', 'N_points_inv': 'N_POINTS_INV', 'Eps_limit_cc': 'EPS_LIMIT_CC', 'Colzero_threshold': 'COLZERO_THRESHOLD', 'Eps_mu': 'EPS_MU', 'Eps_fermi': 'EPS_FERMI', 'Eps_decay': 'EPS_DECAY', 'Transport_method': 'TRANSPORT_METHOD', 'Eps_limit': 'EPS_LIMIT'}
        self._subsections = {'PEXSI': 'PEXSI', 'PRINT': 'PRINT', 'BEYN': 'BEYN'}
        self._repeated_subsections = {'CONTACT': '_contact1'}
        self._attributes = ['CONTACT_list']

    def CONTACT_add(self, section_parameters=None):
        new_section = _contact1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONTACT_list.append(new_section)
        return new_section

