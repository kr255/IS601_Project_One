from Calculator import Calculator
from Operations import Mean

class StatisticsCalculator(Calculator):

    def __init__(self):
        self._result = 0.0
        super().__init__()
        pass

    def mean(self, listofnumbers):
        return Mean.mean(listofnumbers)
        # print(self._result)


