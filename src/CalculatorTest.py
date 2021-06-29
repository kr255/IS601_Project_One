import unittest
from Calculator import Calculator
from BasicArithmitic import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_instantiate_calculator(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_addition(self):
        calc = Calculator()
        self.assertisEqual(calc.addtion(2+2), 4)

    def test_subtraction(self):
        calc = Calculator()
        self.assertisEqual(calc.sub(2-2), 0)

if __name__ == '__main__':
    unittest.main()
