import unittest
import os
from diskspace import *

class TestDiskspace(unittest.TestCase):

 def test_subprocess_check_output(self):
    command = 'ls'
    check = subprocess_check_output(command)
    self.assertEqual(subprocess_check_output(command), check)

 def test_bytes_to_readable(self):
    command = bytes_to_readable(512)
    self.assertEqual(command, '256.00Kb')
    self.assertNotEqual(command, '512.00Kb')


if __name__ == '__main__':
    unittest.main()
