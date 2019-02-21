from pycp2k.inputsection import InputSection


class _avbmc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pbias = None
        self.Avbmc_atom = None
        self.Avbmc_rmin = None
        self.Avbmc_rmax = None
        self._name = "AVBMC"
        self._keywords = {'Pbias': 'PBIAS', 'Avbmc_rmin': 'AVBMC_RMIN', 'Avbmc_atom': 'AVBMC_ATOM', 'Avbmc_rmax': 'AVBMC_RMAX'}

