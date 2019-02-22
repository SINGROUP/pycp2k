from pycp2k.inputsection import InputSection
from ._distance1 import _distance1
from ._angle2 import _angle2
from ._torsion3 import _torsion3
from ._coordination1 import _coordination1
from ._population1 import _population1
from ._gyration_radius1 import _gyration_radius1
from ._distance_point_plane1 import _distance_point_plane1
from ._angle_plane_plane1 import _angle_plane_plane1
from ._bond_rotation1 import _bond_rotation1
from ._distance_function1 import _distance_function1
from ._qparm1 import _qparm1
from ._hydronium_shell1 import _hydronium_shell1
from ._hydronium_distance1 import _hydronium_distance1
from ._acid_hydronium_distance1 import _acid_hydronium_distance1
from ._acid_hydronium_shell1 import _acid_hydronium_shell1
from ._rmsd1 import _rmsd1
from ._xyz_diag1 import _xyz_diag1
from ._xyz_outerdiag1 import _xyz_outerdiag1
from ._u1 import _u1
from ._wc1 import _wc1
from ._hbp1 import _hbp1
from ._ring_puckering1 import _ring_puckering1
from ._conditioned_distance1 import _conditioned_distance1
from ._reaction_path1 import _reaction_path1
from ._distance_from_path1 import _distance_from_path1
from ._combine_colvar1 import _combine_colvar1
from ._print51 import _print51
from ._colvar_func_info4 import _colvar_func_info4


class _colvar5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.DISTANCE = _distance1()
        self.ANGLE = _angle2()
        self.TORSION = _torsion3()
        self.COORDINATION = _coordination1()
        self.POPULATION = _population1()
        self.GYRATION_RADIUS = _gyration_radius1()
        self.DISTANCE_POINT_PLANE = _distance_point_plane1()
        self.ANGLE_PLANE_PLANE = _angle_plane_plane1()
        self.BOND_ROTATION = _bond_rotation1()
        self.DISTANCE_FUNCTION = _distance_function1()
        self.QPARM = _qparm1()
        self.HYDRONIUM_SHELL = _hydronium_shell1()
        self.HYDRONIUM_DISTANCE = _hydronium_distance1()
        self.ACID_HYDRONIUM_DISTANCE = _acid_hydronium_distance1()
        self.ACID_HYDRONIUM_SHELL = _acid_hydronium_shell1()
        self.RMSD = _rmsd1()
        self.XYZ_DIAG = _xyz_diag1()
        self.XYZ_OUTERDIAG = _xyz_outerdiag1()
        self.U = _u1()
        self.WC = _wc1()
        self.HBP = _hbp1()
        self.RING_PUCKERING = _ring_puckering1()
        self.CONDITIONED_DISTANCE = _conditioned_distance1()
        self.REACTION_PATH = _reaction_path1()
        self.DISTANCE_FROM_PATH = _distance_from_path1()
        self.COMBINE_COLVAR = _combine_colvar1()
        self.PRINT_list = []
        self.COLVAR_FUNC_INFO = _colvar_func_info4()
        self._name = "COLVAR"
        self._subsections = {'REACTION_PATH': 'REACTION_PATH', 'BOND_ROTATION': 'BOND_ROTATION', 'COLVAR_FUNC_INFO': 'COLVAR_FUNC_INFO', 'CONDITIONED_DISTANCE': 'CONDITIONED_DISTANCE', 'GYRATION_RADIUS': 'GYRATION_RADIUS', 'POPULATION': 'POPULATION', 'WC': 'WC', 'RING_PUCKERING': 'RING_PUCKERING', 'ANGLE_PLANE_PLANE': 'ANGLE_PLANE_PLANE', 'HBP': 'HBP', 'TORSION': 'TORSION', 'COORDINATION': 'COORDINATION', 'HYDRONIUM_SHELL': 'HYDRONIUM_SHELL', 'XYZ_DIAG': 'XYZ_DIAG', 'QPARM': 'QPARM', 'DISTANCE_POINT_PLANE': 'DISTANCE_POINT_PLANE', 'ACID_HYDRONIUM_DISTANCE': 'ACID_HYDRONIUM_DISTANCE', 'DISTANCE': 'DISTANCE', 'U': 'U', 'ACID_HYDRONIUM_SHELL': 'ACID_HYDRONIUM_SHELL', 'DISTANCE_FROM_PATH': 'DISTANCE_FROM_PATH', 'COMBINE_COLVAR': 'COMBINE_COLVAR', 'RMSD': 'RMSD', 'HYDRONIUM_DISTANCE': 'HYDRONIUM_DISTANCE', 'XYZ_OUTERDIAG': 'XYZ_OUTERDIAG', 'DISTANCE_FUNCTION': 'DISTANCE_FUNCTION', 'ANGLE': 'ANGLE'}
        self._repeated_subsections = {'PRINT': '_print51'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print51()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

