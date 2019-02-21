from pycp2k.inputsection import InputSection
from ._xc_grid2 import _xc_grid2
from ._xc_functional2 import _xc_functional2
from ._hf3 import _hf3
from ._wf_correlation2 import _wf_correlation2
from ._adiabatic_rescaling2 import _adiabatic_rescaling2
from ._xc_potential2 import _xc_potential2
from ._vdw_potential2 import _vdw_potential2


class _xc2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Density_cutoff = None
        self.Gradient_cutoff = None
        self.Density_smooth_cutoff_range = None
        self.Tau_cutoff = None
        self.Functional_routine = None
        self.XC_GRID = _xc_grid2()
        self.XC_FUNCTIONAL = _xc_functional2()
        self.HF_list = []
        self.WF_CORRELATION_list = []
        self.ADIABATIC_RESCALING = _adiabatic_rescaling2()
        self.XC_POTENTIAL = _xc_potential2()
        self.VDW_POTENTIAL = _vdw_potential2()
        self._name = "XC"
        self._keywords = {'Gradient_cutoff': 'GRADIENT_CUTOFF', 'Density_smooth_cutoff_range': 'DENSITY_SMOOTH_CUTOFF_RANGE', 'Functional_routine': 'FUNCTIONAL_ROUTINE', 'Tau_cutoff': 'TAU_CUTOFF', 'Density_cutoff': 'DENSITY_CUTOFF'}
        self._subsections = {'VDW_POTENTIAL': 'VDW_POTENTIAL', 'ADIABATIC_RESCALING': 'ADIABATIC_RESCALING', 'XC_FUNCTIONAL': 'XC_FUNCTIONAL', 'XC_POTENTIAL': 'XC_POTENTIAL', 'XC_GRID': 'XC_GRID'}
        self._repeated_subsections = {'HF': '_hf3', 'WF_CORRELATION': '_wf_correlation2'}
        self._attributes = ['HF_list', 'WF_CORRELATION_list']

    def HF_add(self, section_parameters=None):
        new_section = _hf3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.HF_list.append(new_section)
        return new_section

    def WF_CORRELATION_add(self, section_parameters=None):
        new_section = _wf_correlation2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WF_CORRELATION_list.append(new_section)
        return new_section

