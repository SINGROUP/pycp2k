from pycp2k.inputsection import InputSection
from ._xc_grid3 import _xc_grid3
from ._xc_functional3 import _xc_functional3
from ._hf5 import _hf5
from ._wf_correlation3 import _wf_correlation3
from ._adiabatic_rescaling3 import _adiabatic_rescaling3
from ._xc_potential3 import _xc_potential3
from ._vdw_potential3 import _vdw_potential3


class _xc3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Density_cutoff = None
        self.Gradient_cutoff = None
        self.Density_smooth_cutoff_range = None
        self.Tau_cutoff = None
        self.Functional_routine = None
        self.XC_GRID = _xc_grid3()
        self.XC_FUNCTIONAL = _xc_functional3()
        self.HF_list = []
        self.WF_CORRELATION_list = []
        self.ADIABATIC_RESCALING = _adiabatic_rescaling3()
        self.XC_POTENTIAL = _xc_potential3()
        self.VDW_POTENTIAL = _vdw_potential3()
        self._name = "XC"
        self._keywords = {'Gradient_cutoff': 'GRADIENT_CUTOFF', 'Density_smooth_cutoff_range': 'DENSITY_SMOOTH_CUTOFF_RANGE', 'Functional_routine': 'FUNCTIONAL_ROUTINE', 'Tau_cutoff': 'TAU_CUTOFF', 'Density_cutoff': 'DENSITY_CUTOFF'}
        self._subsections = {'VDW_POTENTIAL': 'VDW_POTENTIAL', 'ADIABATIC_RESCALING': 'ADIABATIC_RESCALING', 'XC_FUNCTIONAL': 'XC_FUNCTIONAL', 'XC_POTENTIAL': 'XC_POTENTIAL', 'XC_GRID': 'XC_GRID'}
        self._repeated_subsections = {'HF': '_hf5', 'WF_CORRELATION': '_wf_correlation3'}
        self._attributes = ['HF_list', 'WF_CORRELATION_list']

    def HF_add(self, section_parameters=None):
        new_section = _hf5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HF_list.append(new_section)
        return new_section

    def WF_CORRELATION_add(self, section_parameters=None):
        new_section = _wf_correlation3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WF_CORRELATION_list.append(new_section)
        return new_section

