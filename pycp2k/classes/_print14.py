from pycp2k.inputsection import InputSection
from ._energy6 import _energy6
from ._projected_area_2_avg1 import _projected_area_2_avg1
from ._winding_number_2_avg1 import _winding_number_2_avg1
from ._moment_of_inertia_avg1 import _moment_of_inertia_avg1
from ._rdf2 import _rdf2
from ._rho2 import _rho2
from ._projected_area1 import _projected_area1
from ._winding_number1 import _winding_number1
from ._moment_of_inertia1 import _moment_of_inertia1
from ._plength1 import _plength1
from ._action1 import _action1
from ._coordinates1 import _coordinates1
from ._perm2 import _perm2
from ._forces1 import _forces1
from ._accepts1 import _accepts1
from ._forces_inst1 import _forces_inst1


class _print14(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ENERGY = _energy6()
        self.PROJECTED_AREA_2_AVG = _projected_area_2_avg1()
        self.WINDING_NUMBER_2_AVG = _winding_number_2_avg1()
        self.MOMENT_OF_INERTIA_AVG = _moment_of_inertia_avg1()
        self.RDF = _rdf2()
        self.RHO = _rho2()
        self.PROJECTED_AREA = _projected_area1()
        self.WINDING_NUMBER = _winding_number1()
        self.MOMENT_OF_INERTIA = _moment_of_inertia1()
        self.PLENGTH = _plength1()
        self.ACTION = _action1()
        self.COORDINATES = _coordinates1()
        self.PERM = _perm2()
        self.FORCES = _forces1()
        self.ACCEPTS = _accepts1()
        self.FORCES_INST = _forces_inst1()
        self._name = "PRINT"
        self._subsections = {'PROJECTED_AREA': 'PROJECTED_AREA', 'PERM': 'PERM', 'ENERGY': 'ENERGY', 'COORDINATES': 'COORDINATES', 'MOMENT_OF_INERTIA_AVG': 'MOMENT_OF_INERTIA_AVG', 'FORCES_INST': 'FORCES_INST', 'FORCES': 'FORCES', 'ACCEPTS': 'ACCEPTS', 'WINDING_NUMBER': 'WINDING_NUMBER', 'RDF': 'RDF', 'MOMENT_OF_INERTIA': 'MOMENT_OF_INERTIA', 'PROJECTED_AREA_2_AVG': 'PROJECTED_AREA_2_AVG', 'WINDING_NUMBER_2_AVG': 'WINDING_NUMBER_2_AVG', 'PLENGTH': 'PLENGTH', 'ACTION': 'ACTION', 'RHO': 'RHO'}

