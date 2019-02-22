from pycp2k.inputsection import InputSection


class _rho1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Nbin = None
        self.Min_cycle_lengths_wdg = None
        self.Min_cycle_lengths_non = None
        self.Min_cycle_lengths_all = None
        self.Atom_number = None
        self.Projected_area_2 = None
        self.Winding_number_2 = None
        self.Winding_cycle_2 = None
        self.Moment_of_inertia = None
        self._name = "RHO"
        self._keywords = {'Min_cycle_lengths_wdg': 'MIN_CYCLE_LENGTHS_WDG', 'Nbin': 'NBIN', 'Winding_cycle_2': 'WINDING_CYCLE_2', 'Winding_number_2': 'WINDING_NUMBER_2', 'Projected_area_2': 'PROJECTED_AREA_2', 'Min_cycle_lengths_all': 'MIN_CYCLE_LENGTHS_ALL', 'Min_cycle_lengths_non': 'MIN_CYCLE_LENGTHS_NON', 'Moment_of_inertia': 'MOMENT_OF_INERTIA', 'Atom_number': 'ATOM_NUMBER'}
        self._attributes = ['Section_parameters']

