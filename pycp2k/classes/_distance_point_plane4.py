from pycp2k.inputsection import InputSection
from ._point58 import _point58


class _distance_point_plane4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pbc = None
        self.Atoms_plane = None
        self.Atom_point = None
        self.POINT_list = []
        self._name = "DISTANCE_POINT_PLANE"
        self._keywords = {'Atoms_plane': 'ATOMS_PLANE', 'Pbc': 'PBC', 'Atom_point': 'ATOM_POINT'}
        self._repeated_subsections = {'POINT': '_point58'}
        self._aliases = {'Points_plane': 'Atoms_plane', 'Point_point': 'Atom_point'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point58()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def Points_plane(self):
        """
        See documentation for Atoms_plane
        """
        return self.Atoms_plane

    @property
    def Point_point(self):
        """
        See documentation for Atom_point
        """
        return self.Atom_point

    @Points_plane.setter
    def Points_plane(self, value):
        self.Atoms_plane = value

    @Point_point.setter
    def Point_point(self, value):
        self.Atom_point = value
