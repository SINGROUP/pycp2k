from pycp2k.inputsection import InputSection
from ._ub1 import _ub1


class _bend1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Kind = None
        self.K = None
        self.Cb = None
        self.R012 = None
        self.R032 = None
        self.Kbs12 = None
        self.Kbs32 = None
        self.Kss = None
        self.Theta0 = None
        self.Legendre = None
        self.UB = _ub1()
        self._name = "BEND"
        self._keywords = {'Cb': 'CB', 'Kbs12': 'KBS12', 'Atoms': 'ATOMS', 'Kbs32': 'KBS32', 'Legendre': 'LEGENDRE', 'Kind': 'KIND', 'Theta0': 'THETA0', 'R032': 'R032', 'Kss': 'KSS', 'K': 'K', 'R012': 'R012'}
        self._subsections = {'UB': 'UB'}

