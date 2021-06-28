import unittest
import Calculator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_instantiate_calculator(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_addition(self):
        calc = Calculator()
        self.assertisEqual(calc.addtion(2+2), )

if __name__ == '__main__':
    unittest.main()
