from pycp2k.inputsection import InputSection
from ._ceperley1 import _ceperley1
from ._worm1 import _worm1
from ._rdf1 import _rdf1
from ._rho1 import _rho1
from ._coord8 import _coord8
from ._perm1 import _perm1
from ._averages2 import _averages2
from ._force6 import _force6
from ._rng_state1 import _rng_state1
from ._print14 import _print14


class _helium1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Helium_only = None
        self.Interaction_pot_scan = None
        self.Num_env = None
        self.Potential_file_name = None
        self.Get_forces = None
        self.Solute_interaction = None
        self.Natoms = None
        self.Nbeads = None
        self.Rng_seed = None
        self.N_inner = None
        self.N_outer = None
        self.Sampling_method = None
        self.Periodic = None
        self.Cell_size = None
        self.Cell_shape = None
        self.Droplet_radius = None
        self.Density = None
        self.Presample = None
        self.CEPERLEY = _ceperley1()
        self.WORM = _worm1()
        self.RDF = _rdf1()
        self.RHO = _rho1()
        self.COORD = _coord8()
        self.PERM = _perm1()
        self.AVERAGES = _averages2()
        self.FORCE = _force6()
        self.RNG_STATE = _rng_state1()
        self.PRINT = _print14()
        self._name = "HELIUM"
        self._keywords = {'Potential_file_name': 'POTENTIAL_FILE_NAME', 'Get_forces': 'GET_FORCES', 'Helium_only': 'HELIUM_ONLY', 'Rng_seed': 'RNG_SEED', 'Presample': 'PRESAMPLE', 'N_outer': 'N_OUTER', 'Solute_interaction': 'SOLUTE_INTERACTION', 'Droplet_radius': 'DROPLET_RADIUS', 'Interaction_pot_scan': 'INTERACTION_POT_SCAN', 'N_inner': 'N_INNER', 'Cell_shape': 'CELL_SHAPE', 'Nbeads': 'NBEADS', 'Cell_size': 'CELL_SIZE', 'Sampling_method': 'SAMPLING_METHOD', 'Periodic': 'PERIODIC', 'Density': 'DENSITY', 'Natoms': 'NATOMS', 'Num_env': 'NUM_ENV'}
        self._subsections = {'RDF': 'RDF', 'RNG_STATE': 'RNG_STATE', 'PERM': 'PERM', 'CEPERLEY': 'CEPERLEY', 'WORM': 'WORM', 'COORD': 'COORD', 'FORCE': 'FORCE', 'AVERAGES': 'AVERAGES', 'PRINT': 'PRINT', 'RHO': 'RHO'}
        self._aliases = {'Irot': 'N_outer', 'Inorot': 'N_inner'}
        self._attributes = ['Section_parameters']


    @property
    def Inorot(self):
        """
        See documentation for N_inner
        """
        return self.N_inner

    @property
    def Irot(self):
        """
        See documentation for N_outer
        """
        return self.N_outer

    @Inorot.setter
    def Inorot(self, value):
        self.N_inner = value

    @Irot.setter
    def Irot(self, value):
        self.N_outer = value
