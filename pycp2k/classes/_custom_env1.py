from pycp2k.inputsection import InputSection


class _custom_env1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Efield_file_name = None
        self.Timestep = None
        self._name = "CUSTOM_ENV"
        self._keywords = {'Efield_file_name': 'EFIELD_FILE_NAME', 'Timestep': 'TIMESTEP'}

