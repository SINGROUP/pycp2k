from pycp2k.inputsection import InputSection
from ._basis1 import _basis1


class _shg_integrals_test1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Abc = None
        self.Nab_min = None
        self.Nrep = None
        self.Check_accuracy = None
        self.Accuracy_level = None
        self.Calculate_derivatives = None
        self.Test_overlap = None
        self.Test_coulomb = None
        self.Test_verf = None
        self.Test_verfc = None
        self.Test_vgauss = None
        self.Test_gauss = None
        self.Test_ra2m = None
        self.M = None
        self.Test_overlap_aba = None
        self.Test_overlap_abb = None
        self.BASIS_list = []
        self._name = "SHG_INTEGRALS_TEST"
        self._keywords = {'Nab_min': 'NAB_MIN', 'Check_accuracy': 'CHECK_ACCURACY', 'Abc': 'ABC', 'Test_verf': 'TEST_VERF', 'Test_overlap_aba': 'TEST_OVERLAP_ABA', 'Calculate_derivatives': 'CALCULATE_DERIVATIVES', 'Test_overlap': 'TEST_OVERLAP', 'Test_coulomb': 'TEST_COULOMB', 'Test_vgauss': 'TEST_VGAUSS', 'Test_overlap_abb': 'TEST_OVERLAP_ABB', 'Test_verfc': 'TEST_VERFC', 'Test_ra2m': 'TEST_RA2M', 'Test_gauss': 'TEST_GAUSS', 'M': 'M', 'Accuracy_level': 'ACCURACY_LEVEL', 'Nrep': 'NREP'}
        self._repeated_subsections = {'BASIS': '_basis1'}
        self._attributes = ['Section_parameters', 'BASIS_list']

    def BASIS_add(self, section_parameters=None):
        new_section = _basis1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.BASIS_list.append(new_section)
        return new_section

