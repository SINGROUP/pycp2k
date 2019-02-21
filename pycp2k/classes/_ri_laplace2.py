from pycp2k.inputsection import InputSection


class _ri_laplace2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Quadrature_points = None
        self.Size_integ_group = None
        self._name = "RI_LAPLACE"
        self._keywords = {'Size_integ_group': 'SIZE_INTEG_GROUP', 'Quadrature_points': 'QUADRATURE_POINTS'}
        self._aliases = {'Laplace_group_size': 'Size_integ_group', 'Laplace_num_quad_points': 'Quadrature_points'}


    @property
    def Laplace_num_quad_points(self):
        """
        See documentation for Quadrature_points
        """
        return self.Quadrature_points

    @property
    def Laplace_group_size(self):
        """
        See documentation for Size_integ_group
        """
        return self.Size_integ_group

    @Laplace_num_quad_points.setter
    def Laplace_num_quad_points(self, value):
        self.Quadrature_points = value

    @Laplace_group_size.setter
    def Laplace_group_size(self, value):
        self.Size_integ_group = value
