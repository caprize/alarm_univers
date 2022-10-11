import unittest
from main import *
class TestMethods(unittest.TestCase):

    def test_time(self):
        a = checkTimeforValid("12:30")
        b = checkTimeforValid("12-30")
        c = checkTimeforValid("aa:30")
        self.assertEqual(a, 3)
        self.assertEqual(b, 2)
        self.assertEqual(c, 2)

if __name__ == '__main__':
    unittest.main()