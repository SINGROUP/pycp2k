from pycp2k.inputsection import InputSection


class _update1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Result_mo_index = None
        self.Result_marked_state = None
        self.Result_spin_index = None
        self.Result_scale = None
        self.Orig_mo_index = None
        self.Orig_marked_state = None
        self.Orig_spin_index = None
        self.Orig_scale = None
        self.Orig_is_virtual = None
        self._name = "UPDATE"
        self._keywords = {'Result_scale': 'RESULT_SCALE', 'Orig_marked_state': 'ORIG_MARKED_STATE', 'Result_spin_index': 'RESULT_SPIN_INDEX', 'Orig_scale': 'ORIG_SCALE', 'Orig_is_virtual': 'ORIG_IS_VIRTUAL', 'Result_marked_state': 'RESULT_MARKED_STATE', 'Orig_mo_index': 'ORIG_MO_INDEX', 'Result_mo_index': 'RESULT_MO_INDEX', 'Orig_spin_index': 'ORIG_SPIN_INDEX'}

