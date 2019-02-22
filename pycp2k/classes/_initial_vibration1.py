from pycp2k.inputsection import InputSection


class _initial_vibration1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Vib_eigs_file_name = None
        self.Phase = None
        self._name = "INITIAL_VIBRATION"
        self._keywords = {'Vib_eigs_file_name': 'VIB_EIGS_FILE_NAME', 'Phase': 'PHASE'}

