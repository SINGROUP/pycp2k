from pycp2k.inputsection import InputSection
from ._lbfgs2 import _lbfgs2
from ._cg2 import _cg2
from ._bfgs2 import _bfgs2
from ._print2 import _print2


class _rot_opt1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Optimizer = None
        self.Max_iter = None
        self.Max_dr = None
        self.Max_force = None
        self.Rms_dr = None
        self.Rms_force = None
        self.Step_start_val = None
        self.LBFGS = _lbfgs2()
        self.CG = _cg2()
        self.BFGS = _bfgs2()
        self.PRINT_list = []
        self._name = "ROT_OPT"
        self._keywords = {'Max_force': 'MAX_FORCE', 'Rms_dr': 'RMS_DR', 'Step_start_val': 'STEP_START_VAL', 'Rms_force': 'RMS_FORCE', 'Optimizer': 'OPTIMIZER', 'Max_dr': 'MAX_DR', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'BFGS': 'BFGS', 'CG': 'CG', 'LBFGS': 'LBFGS'}
        self._repeated_subsections = {'PRINT': '_print2'}
        self._aliases = {'Minimizer': 'Optimizer'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print2()
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
