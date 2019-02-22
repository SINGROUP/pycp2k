from pycp2k.inputsection import InputSection


class _external_vxc2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_vxc = None
        self.Grid_tol = None
        self._name = "EXTERNAL_VXC"
        self._keywords = {'Grid_tol': 'GRID_TOL', 'File_vxc': 'FILE_VXC'}

