from pycp2k.inputsection import InputSection
from ._machine_learning1 import _machine_learning1
from ._print20 import _print20
from ._line_search5 import _line_search5


class _pao1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_pao = None
        self.Mixing = None
        self.Max_pao = None
        self.Max_cycles = None
        self.Parameterization = None
        self.Regularization = None
        self.Penalty_distance = None
        self.Penalty_strength = None
        self.Precondition = None
        self.Eps_pgf = None
        self.Preopt_dm_file = None
        self.Restart_file = None
        self.Check_gradient_tol = None
        self.Num_gradient_eps = None
        self.Num_gradient_order = None
        self.Check_unitary_tol = None
        self.Linpot_precondition_delta = None
        self.Linpot_initguess_delta = None
        self.Linpot_regularization_delta = None
        self.Linpot_regularization_strength = None
        self.Optimizer = None
        self.Cg_init_steps = None
        self.Cg_reset_limit = None
        self.MACHINE_LEARNING = _machine_learning1()
        self.PRINT_list = []
        self.LINE_SEARCH = _line_search5()
        self._name = "PAO"
        self._keywords = {'Preopt_dm_file': 'PREOPT_DM_FILE', 'Max_cycles': 'MAX_CYCLES', 'Check_unitary_tol': 'CHECK_UNITARY_TOL', 'Linpot_initguess_delta': 'LINPOT_INITGUESS_DELTA', 'Penalty_distance': 'PENALTY_DISTANCE', 'Max_pao': 'MAX_PAO', 'Precondition': 'PRECONDITION', 'Linpot_precondition_delta': 'LINPOT_PRECONDITION_DELTA', 'Restart_file': 'RESTART_FILE', 'Eps_pgf': 'EPS_PGF', 'Parameterization': 'PARAMETERIZATION', 'Num_gradient_eps': 'NUM_GRADIENT_EPS', 'Linpot_regularization_strength': 'LINPOT_REGULARIZATION_STRENGTH', 'Penalty_strength': 'PENALTY_STRENGTH', 'Regularization': 'REGULARIZATION', 'Check_gradient_tol': 'CHECK_GRADIENT_TOL', 'Num_gradient_order': 'NUM_GRADIENT_ORDER', 'Cg_reset_limit': 'CG_RESET_LIMIT', 'Eps_pao': 'EPS_PAO', 'Optimizer': 'OPTIMIZER', 'Mixing': 'MIXING', 'Cg_init_steps': 'CG_INIT_STEPS', 'Linpot_regularization_delta': 'LINPOT_REGULARIZATION_DELTA'}
        self._subsections = {'LINE_SEARCH': 'LINE_SEARCH', 'MACHINE_LEARNING': 'MACHINE_LEARNING'}
        self._repeated_subsections = {'PRINT': '_print20'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print20()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

