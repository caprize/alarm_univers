import unittest
from main import *
class TestMethods(unittest.TestCase):

    def test_time(self):
        a = checkTimeforValid("12:30")
        b = checkTimeforValid("12-30")
        c = checkTimeforValid("aa:30")
        d = checkTimeforValid("12:60")
        self.assertEqual(a, 3)
        self.assertEqual(b, 2)
        self.assertEqual(c, 2)
        self.assertEqual(d, 2)

    def test_conf(self):
        a = checkConftoValid("s")
        b = checkConftoValid("y")
        c = checkConftoValid("N")
        self.assertEqual(a, 6)
        self.assertEqual(b, 4)
        self.assertEqual(c, 5)
    def test_path(self):
        a = checkForvalidpath("/Users")
        b = checkForvalidpath("/Uswes")
        self.assertEqual(a, 8)
        self.assertEqual(b, 9)

if __name__ == '__main__':
    unittest.main()
