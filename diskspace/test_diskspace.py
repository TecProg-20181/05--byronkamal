import unittest
import os
import subprocess
from diskspace import *

class TestDiskspace(unittest.TestCase):

 def test_subprocess_check_output(self):
    command = 'ls'
    method = subprocess.check_output(command)
    self.assertEqual(subprocess_check_output(command), method)

 def test_bytes_to_readable(self):
    command = bytes_to_readable(512)
    self.assertEqual(command, '256.00Kb')
    self.assertNotEqual(command, '512.00Kb')

 def test_show_space_list(self):
    self.assertIsNone(show_space_list(directory='.', depth=-1, order=True))


suite = unittest.TestLoader().loadTestsFromTestCase(TestDiskspace)
unittest.TextTestRunner(verbosity=2).run(suite)
