from pycp2k.inputsection import InputSection


class _qm_kind3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Mm_index = []
        self._name = "QM_KIND"
        self._repeated_keywords = {'Mm_index': 'MM_INDEX'}
        self._attributes = ['Section_parameters']

