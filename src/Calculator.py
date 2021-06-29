from BasicArithmitic import *
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
