from pycp2k.inputsection import InputSection
from ._constraint2 import _constraint2
from ._restraint8 import _restraint8
from ._sphere_sampling1 import _sphere_sampling1
from ._slab_sampling1 import _slab_sampling1
from ._print62 import _print62


class _resp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Stride = None
        self.Integer_total_charge = None
        self.Restrain_heavies_to_zero = None
        self.Restrain_heavies_strength = None
        self.Width = None
        self.Use_repeat_method = None
        self.CONSTRAINT_list = []
        self.RESTRAINT_list = []
        self.SPHERE_SAMPLING = _sphere_sampling1()
        self.SLAB_SAMPLING_list = []
        self.PRINT = _print62()
        self._name = "RESP"
        self._keywords = {'Use_repeat_method': 'USE_REPEAT_METHOD', 'Width': 'WIDTH', 'Restrain_heavies_to_zero': 'RESTRAIN_HEAVIES_TO_ZERO', 'Restrain_heavies_strength': 'RESTRAIN_HEAVIES_STRENGTH', 'Integer_total_charge': 'INTEGER_TOTAL_CHARGE', 'Stride': 'STRIDE'}
        self._subsections = {'SPHERE_SAMPLING': 'SPHERE_SAMPLING', 'PRINT': 'PRINT'}
        self._repeated_subsections = {'RESTRAINT': '_restraint8', 'CONSTRAINT': '_constraint2', 'SLAB_SAMPLING': '_slab_sampling1'}
        self._attributes = ['CONSTRAINT_list', 'RESTRAINT_list', 'SLAB_SAMPLING_list']

    def RESTRAINT_add(self, section_parameters=None):
        new_section = _restraint8()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RESTRAINT_list.append(new_section)
        return new_section

    def CONSTRAINT_add(self, section_parameters=None):
        new_section = _constraint2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONSTRAINT_list.append(new_section)
        return new_section

    def SLAB_SAMPLING_add(self, section_parameters=None):
        new_section = _slab_sampling1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.SLAB_SAMPLING_list.append(new_section)
        return new_section

