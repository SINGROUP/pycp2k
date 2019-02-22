from pycp2k.inputsection import InputSection
from ._qm_non_adaptive1 import _qm_non_adaptive1
from ._buffer_non_adaptive1 import _buffer_non_adaptive1
from ._buffer_links1 import _buffer_links1
from ._restart_info1 import _restart_info1
from ._print42 import _print42


class _force_mixing1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Momentum_conservation_type = None
        self.Momentum_conservation_region = None
        self.R_core = None
        self.R_qm = None
        self.Qm_extended_seed_is_only_core_list = None
        self.R_buf = None
        self.Qm_kind_element_mapping = []
        self.Max_n_qm = None
        self.Adaptive_exclude_molecules = None
        self.Extended_delta_charge = None
        self.QM_NON_ADAPTIVE_list = []
        self.BUFFER_NON_ADAPTIVE_list = []
        self.BUFFER_LINKS_list = []
        self.RESTART_INFO = _restart_info1()
        self.PRINT = _print42()
        self._name = "FORCE_MIXING"
        self._keywords = {'Momentum_conservation_region': 'MOMENTUM_CONSERVATION_REGION', 'R_core': 'R_CORE', 'Qm_extended_seed_is_only_core_list': 'QM_EXTENDED_SEED_IS_ONLY_CORE_LIST', 'R_qm': 'R_QM', 'Adaptive_exclude_molecules': 'ADAPTIVE_EXCLUDE_MOLECULES', 'Momentum_conservation_type': 'MOMENTUM_CONSERVATION_TYPE', 'R_buf': 'R_BUF', 'Extended_delta_charge': 'EXTENDED_DELTA_CHARGE', 'Max_n_qm': 'MAX_N_QM'}
        self._repeated_keywords = {'Qm_kind_element_mapping': 'QM_KIND_ELEMENT_MAPPING'}
        self._subsections = {'RESTART_INFO': 'RESTART_INFO', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'BUFFER_NON_ADAPTIVE': '_buffer_non_adaptive1', 'BUFFER_LINKS': '_buffer_links1', 'QM_NON_ADAPTIVE': '_qm_non_adaptive1'}
        self._attributes = ['Section_parameters', 'QM_NON_ADAPTIVE_list', 'BUFFER_NON_ADAPTIVE_list', 'BUFFER_LINKS_list']

    def BUFFER_NON_ADAPTIVE_add(self, section_parameters=None):
        new_section = _buffer_non_adaptive1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BUFFER_NON_ADAPTIVE_list.append(new_section)
        return new_section

    def BUFFER_LINKS_add(self, section_parameters=None):
        new_section = _buffer_links1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BUFFER_LINKS_list.append(new_section)
        return new_section

    def QM_NON_ADAPTIVE_add(self, section_parameters=None):
        new_section = _qm_non_adaptive1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.QM_NON_ADAPTIVE_list.append(new_section)
        return new_section

