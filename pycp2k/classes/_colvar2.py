from pycp2k.inputsection import InputSection
from ._distance2 import _distance2
from ._angle3 import _angle3
from ._torsion4 import _torsion4
from ._coordination2 import _coordination2
from ._population2 import _population2
from ._gyration_radius2 import _gyration_radius2
from ._distance_point_plane2 import _distance_point_plane2
from ._angle_plane_plane2 import _angle_plane_plane2
from ._bond_rotation2 import _bond_rotation2
from ._distance_function2 import _distance_function2
from ._qparm2 import _qparm2
from ._hydronium_shell2 import _hydronium_shell2
from ._hydronium_distance2 import _hydronium_distance2
from ._acid_hydronium_distance2 import _acid_hydronium_distance2
from ._acid_hydronium_shell2 import _acid_hydronium_shell2
from ._rmsd2 import _rmsd2
from ._xyz_diag2 import _xyz_diag2
from ._xyz_outerdiag2 import _xyz_outerdiag2
from ._u2 import _u2
from ._wc2 import _wc2
from ._hbp2 import _hbp2
from ._ring_puckering2 import _ring_puckering2
from ._conditioned_distance2 import _conditioned_distance2
from ._print48 import _print48
from ._colvar_func_info1 import _colvar_func_info1


class _colvar2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DISTANCE = _distance2()
        self.ANGLE = _angle3()
        self.TORSION = _torsion4()
        self.COORDINATION = _coordination2()
        self.POPULATION = _population2()
        self.GYRATION_RADIUS = _gyration_radius2()
        self.DISTANCE_POINT_PLANE = _distance_point_plane2()
        self.ANGLE_PLANE_PLANE = _angle_plane_plane2()
        self.BOND_ROTATION = _bond_rotation2()
        self.DISTANCE_FUNCTION = _distance_function2()
        self.QPARM = _qparm2()
        self.HYDRONIUM_SHELL = _hydronium_shell2()
        self.HYDRONIUM_DISTANCE = _hydronium_distance2()
        self.ACID_HYDRONIUM_DISTANCE = _acid_hydronium_distance2()
        self.ACID_HYDRONIUM_SHELL = _acid_hydronium_shell2()
        self.RMSD = _rmsd2()
        self.XYZ_DIAG = _xyz_diag2()
        self.XYZ_OUTERDIAG = _xyz_outerdiag2()
        self.U = _u2()
        self.WC = _wc2()
        self.HBP = _hbp2()
        self.RING_PUCKERING = _ring_puckering2()
        self.CONDITIONED_DISTANCE = _conditioned_distance2()
        self.PRINT_list = []
        self.COLVAR_FUNC_INFO = _colvar_func_info1()
        self._name = "COLVAR"
        self._subsections = {'BOND_ROTATION': 'BOND_ROTATION', 'COLVAR_FUNC_INFO': 'COLVAR_FUNC_INFO', 'CONDITIONED_DISTANCE': 'CONDITIONED_DISTANCE', 'GYRATION_RADIUS': 'GYRATION_RADIUS', 'POPULATION': 'POPULATION', 'WC': 'WC', 'RING_PUCKERING': 'RING_PUCKERING', 'ANGLE_PLANE_PLANE': 'ANGLE_PLANE_PLANE', 'HBP': 'HBP', 'TORSION': 'TORSION', 'COORDINATION': 'COORDINATION', 'HYDRONIUM_SHELL': 'HYDRONIUM_SHELL', 'XYZ_DIAG': 'XYZ_DIAG', 'QPARM': 'QPARM', 'DISTANCE_POINT_PLANE': 'DISTANCE_POINT_PLANE', 'ACID_HYDRONIUM_DISTANCE': 'ACID_HYDRONIUM_DISTANCE', 'DISTANCE': 'DISTANCE', 'U': 'U', 'ACID_HYDRONIUM_SHELL': 'ACID_HYDRONIUM_SHELL', 'RMSD': 'RMSD', 'HYDRONIUM_DISTANCE': 'HYDRONIUM_DISTANCE', 'XYZ_OUTERDIAG': 'XYZ_OUTERDIAG', 'DISTANCE_FUNCTION': 'DISTANCE_FUNCTION', 'ANGLE': 'ANGLE'}
        self._repeated_subsections = {'PRINT': '_print48'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print48()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

