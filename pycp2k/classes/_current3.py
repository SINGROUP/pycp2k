from pycp2k.inputsection import InputSection
from ._print54 import _print54
from ._interpolator9 import _interpolator9


class _current3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Gauge = None
        self.Gauge_atom_radius = None
        self.Use_old_gauge_atom = None
        self.Orbital_center = None
        self.Common_center = None
        self.Nbox = None
        self.Chi_pbc = None
        self.Force_no_full = None
        self.Selected_states_on_atom_list = []
        self.Selected_states_atom_radius = None
        self.Restart_current = None
        self.PRINT = _print54()
        self.INTERPOLATOR = _interpolator9()
        self._name = "CURRENT"
        self._keywords = {'Gauge': 'GAUGE', 'Nbox': 'NBOX', 'Restart_current': 'RESTART_CURRENT', 'Common_center': 'COMMON_CENTER', 'Gauge_atom_radius': 'GAUGE_ATOM_RADIUS', 'Use_old_gauge_atom': 'USE_OLD_GAUGE_ATOM', 'Selected_states_atom_radius': 'SELECTED_STATES_ATOM_RADIUS', 'Force_no_full': 'FORCE_NO_FULL', 'Chi_pbc': 'CHI_PBC', 'Orbital_center': 'ORBITAL_CENTER'}
        self._repeated_keywords = {'Selected_states_on_atom_list': 'SELECTED_STATES_ON_ATOM_LIST'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'PRINT': 'PRINT'}
        self._attributes = ['Section_parameters']

