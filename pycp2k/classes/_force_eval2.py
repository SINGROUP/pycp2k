from pycp2k.inputsection import InputSection
from ._external_potential1 import _external_potential1
from ._rescale_forces1 import _rescale_forces1
from ._mixed1 import _mixed1
from ._dft1 import _dft1
from ._mm1 import _mm1
from ._qmmm1 import _qmmm1
from ._eip1 import _eip1
from ._bsse1 import _bsse1
from ._subsys1 import _subsys1
from ._properties1 import _properties1
from ._print64 import _print64


class _force_eval2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Stress_tensor = None
        self.Embed = None
        self.EXTERNAL_POTENTIAL_list = []
        self.RESCALE_FORCES = _rescale_forces1()
        self.MIXED = _mixed1()
        self.DFT = _dft1()
        self.MM = _mm1()
        self.QMMM = _qmmm1()
        self.EIP = _eip1()
        self.BSSE = _bsse1()
        self.SUBSYS = _subsys1()
        self.PROPERTIES = _properties1()
        self.PRINT = _print64()
        self._name = "FORCE_EVAL"
        self._keywords = {'Method': 'METHOD', 'Embed': 'EMBED', 'Stress_tensor': 'STRESS_TENSOR'}
        self._subsections = {'PRINT': 'PRINT', 'MIXED': 'MIXED', 'EIP': 'EIP', 'SUBSYS': 'SUBSYS', 'RESCALE_FORCES': 'RESCALE_FORCES', 'PROPERTIES': 'PROPERTIES', 'DFT': 'DFT', 'QMMM': 'QMMM', 'BSSE': 'BSSE', 'MM': 'MM'}
        self._repeated_subsections = {'EXTERNAL_POTENTIAL': '_external_potential1'}
        self._attributes = ['EXTERNAL_POTENTIAL_list']

    def EXTERNAL_POTENTIAL_add(self, section_parameters=None):
        new_section = _external_potential1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.EXTERNAL_POTENTIAL_list.append(new_section)
        return new_section

