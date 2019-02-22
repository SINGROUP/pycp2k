from pycp2k.inputsection import InputSection


class _num2pnt3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_allowed_step = None
        self.Linmin_grad_only = None
        self._name = "2PNT"
        self._keywords = {'Max_allowed_step': 'MAX_ALLOWED_STEP', 'Linmin_grad_only': 'LINMIN_GRAD_ONLY'}

