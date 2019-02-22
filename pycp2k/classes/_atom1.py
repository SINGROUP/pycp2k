from pycp2k.inputsection import InputSection
from ._print68 import _print68
from ._ae_basis1 import _ae_basis1
from ._pp_basis1 import _pp_basis1
from ._method1 import _method1
from ._optimization2 import _optimization2
from ._potential4 import _potential4
from ._powell1 import _powell1


class _atom1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atomic_number = None
        self.Element = None
        self.Run_type = None
        self.Coulomb_integrals = None
        self.Exchange_integrals = None
        self.Core = None
        self.Electron_configuration = []
        self.Max_angular_momentum = None
        self.Calculate_states = None
        self.PRINT = _print68()
        self.AE_BASIS = _ae_basis1()
        self.PP_BASIS = _pp_basis1()
        self.METHOD_list = []
        self.OPTIMIZATION = _optimization2()
        self.POTENTIAL = _potential4()
        self.POWELL = _powell1()
        self._name = "ATOM"
        self._keywords = {'Core': 'CORE', 'Max_angular_momentum': 'MAX_ANGULAR_MOMENTUM', 'Element': 'ELEMENT', 'Coulomb_integrals': 'COULOMB_INTEGRALS', 'Exchange_integrals': 'EXCHANGE_INTEGRALS', 'Run_type': 'RUN_TYPE', 'Calculate_states': 'CALCULATE_STATES', 'Atomic_number': 'ATOMIC_NUMBER'}
        self._repeated_keywords = {'Electron_configuration': 'ELECTRON_CONFIGURATION'}
        self._subsections = {'POWELL': 'POWELL', 'AE_BASIS': 'AE_BASIS', 'PRINT': 'PRINT', 'PP_BASIS': 'PP_BASIS', 'POTENTIAL': 'POTENTIAL', 'OPTIMIZATION': 'OPTIMIZATION'}
        self._repeated_subsections = {'METHOD': '_method1'}
        self._attributes = ['METHOD_list']

    def METHOD_add(self, section_parameters=None):
        new_section = _method1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.METHOD_list.append(new_section)
        return new_section

