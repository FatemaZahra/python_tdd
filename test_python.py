from calc import SimpleCalc
import unittest
import pytest

class Caltests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc_obj.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc_obj.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(self.calc_obj.divide(2, 2), 1)


