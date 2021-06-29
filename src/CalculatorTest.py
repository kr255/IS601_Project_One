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
        self.assertEqual(calc.add(2,2), 4)

    def test_subtraction(self):
        calc = Calculator()
        self.assertEqual(calc.sub(2,2), 0)

    def test_multiplication(self):
        calc = Calculator()
        self.assertEqual(calc.mul(2,2), 4)

    def test_division(self):
        calc = Calculator()
        self.assertEqual(calc.div(2,2), 1)

    def test_square(self):
        calc = Calculator()
        self.assertEqual(calc.square(2), 4)

    def test_squareRootFromBasicArithmitic(self):
        self.assertEqual(squareRoot(16), 4)

    def test_squareRootFromBasicArithmitic(self):
        self.assertEqual(squareRoot(4), 2)

if __name__ == '__main__':
    unittest.main()
