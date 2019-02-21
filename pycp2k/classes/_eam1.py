from pycp2k.inputsection import InputSection


class _eam1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Parm_file_name = None
        self._name = "EAM"
        self._keywords = {'Atoms': 'ATOMS', 'Parm_file_name': 'PARM_FILE_NAME'}
        self._aliases = {'Parmfile': 'Parm_file_name'}


    @property
    def Parmfile(self):
        """
        See documentation for Parm_file_name
        """
        return self.Parm_file_name

    @Parmfile.setter
    def Parmfile(self, value):
        self.Parm_file_name = value
