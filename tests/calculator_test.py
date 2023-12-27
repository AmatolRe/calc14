import unittest
from calculator import copy_array

class TestCopyArray(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(copy_array([1, 2, 3, 4, 5], 2), [3, 4, 5])

if __name__ == '__main__':
    unittest.main()