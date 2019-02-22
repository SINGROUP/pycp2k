from pycp2k.inputsection import InputSection


class _exclude_vdw_list1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Bond = None
        self._name = "EXCLUDE_VDW_LIST"
        self._keywords = {'Bond': 'BOND'}

