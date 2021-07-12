from Operations.Addition import addition
from Operations.Division import divide
from Operations.Multiplication import multiply
from Operations.Square import square
from Operations.SquareRoot import squareRoot
from Operations.Subtraction import subtract


class Calculator:

    def __init__(self):
        self._result = 0
        pass

    def add(self, a, b):
        return addition(a, b)
    def sub(self, a, b):
        return subtract(a, b)
    def div(self, a, b):
        return divide(a, b)
    def mul(self, a, b):
        return multiply(a, b)
    def square(self, a):
        return square(a)
    def squRoot(self, a):
        return squareRoot(a)