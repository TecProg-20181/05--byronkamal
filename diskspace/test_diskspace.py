import unittest
from diskspace import *

class TestDiskspace(unittest.TestCase):


    def test_bytes_to_readable(self):
        command = bytes_to_readable(256)
        self.assertEqual(command, '128.00Kb')
        self.assertNotEqual(command, '256.00Kb')


suite =
unittest.TestLoader().loadTestsFromTestCase(TestDiskspace)
unittest.TextTestRunner(verbosity=2).run(suite)
