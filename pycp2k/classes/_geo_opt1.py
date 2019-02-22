from pycp2k.inputsection import InputSection
from ._lbfgs1 import _lbfgs1
from ._cg1 import _cg1
from ._bfgs1 import _bfgs1
from ._transition_state1 import _transition_state1
from ._print3 import _print3


class _geo_opt1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.Optimizer = None
        self.Max_iter = None
        self.Max_dr = None
        self.Max_force = None
        self.Rms_dr = None
        self.Rms_force = None
        self.Step_start_val = None
        self.LBFGS = _lbfgs1()
        self.CG = _cg1()
        self.BFGS = _bfgs1()
        self.TRANSITION_STATE = _transition_state1()
        self.PRINT_list = []
        self._name = "GEO_OPT"
        self._keywords = {'Max_force': 'MAX_FORCE', 'Rms_dr': 'RMS_DR', 'Step_start_val': 'STEP_START_VAL', 'Rms_force': 'RMS_FORCE', 'Optimizer': 'OPTIMIZER', 'Max_dr': 'MAX_DR', 'Type': 'TYPE', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'TRANSITION_STATE': 'TRANSITION_STATE', 'BFGS': 'BFGS', 'CG': 'CG', 'LBFGS': 'LBFGS'}
        self._repeated_subsections = {'PRINT': '_print3'}
        self._aliases = {'Minimizer': 'Optimizer'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section


    @property
    def Minimizer(self):
        """
        See documentation for Optimizer
        """
        return self.Optimizer

    @Minimizer.setter
    def Minimizer(self, value):
        self.Optimizer = value
