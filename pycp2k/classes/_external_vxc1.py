from pycp2k.inputsection import InputSection


class _external_vxc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_vxc = None
        self._name = "EXTERNAL_VXC"
        self._keywords = {'File_vxc': 'FILE_VXC'}

