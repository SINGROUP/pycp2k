from pycp2k.inputsection import InputSection


class _training_files1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Directory = None
        self.Input_file_name = None
        self._name = "TRAINING_FILES"
        self._keywords = {'Directory': 'DIRECTORY', 'Input_file_name': 'INPUT_FILE_NAME'}

