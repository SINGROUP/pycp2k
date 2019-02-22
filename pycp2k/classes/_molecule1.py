from pycp2k.inputsection import InputSection


class _molecule1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nmol = None
        self.Conn_file_name = None
        self.Conn_file_format = None
        self._name = "MOLECULE"
        self._keywords = {'Conn_file_format': 'CONN_FILE_FORMAT', 'Nmol': 'NMOL', 'Conn_file_name': 'CONN_FILE_NAME'}
        self._aliases = {'Conn_file': 'Conn_file_name', 'Connectivity': 'Conn_file_format'}


    @property
    def Conn_file(self):
        """
        See documentation for Conn_file_name
        """
        return self.Conn_file_name

    @property
    def Connectivity(self):
        """
        See documentation for Conn_file_format
        """
        return self.Conn_file_format

    @Conn_file.setter
    def Conn_file(self, value):
        self.Conn_file_name = value

    @Connectivity.setter
    def Connectivity(self, value):
        self.Conn_file_format = value
