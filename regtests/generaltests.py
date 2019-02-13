from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import (bytes, str, open, super, range, zip, round, input, int, pow, object)

import unittest
import sys
from pycp2k import CP2K


class GeneralTests(unittest.TestCase):

    def test_repeated_keywords(self):
        """Ensures that repeatable keywords are correctly handled.
        """

        # Test that input parser correctly reads repeated keywords
        calc = CP2K()
        calc.parse("./repeated_keywords/template.in")
        force_eval = calc.CP2K_INPUT.FORCE_EVAL_list[0]
        basis_files = force_eval.DFT.Basis_set_file_name
        self.assertEqual(len(basis_files), 2)

        # Test that non-repeatable keywords are replaced instead of repeated
        periodic = force_eval.SUBSYS.CELL.Periodic
        self.assertEqual(periodic, "XYZ")

if __name__ == '__main__':
    suites = []
    suites.append(unittest.TestLoader().loadTestsFromTestCase(GeneralTests))
    alltests = unittest.TestSuite(suites)
    result = unittest.TextTestRunner(verbosity=0).run(alltests)

    # We need to return a non-zero exit code for the gitlab CI to detect errors
    sys.exit(not result.wasSuccessful())
