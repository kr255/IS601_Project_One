from Calculator.Calculator import Calculator
from Operations import Mean, Median, Mode, Variance, StandardDeviation

class StatisticsCalculator(Calculator):

    def __init__(self):
        self._result = 0.0
        super().__init__()
        pass

    def mean(self, listofnumbers):
        return Mean.mean(listofnumbers)
        # print(self._result)
    def median(self, listofnumbers):
        return Median.median(listofnumbers)
    def mode(self, listofnumbers):
        return Mode.mode(listofnumbers)
    def variance(self, listofnumbers):
        return Variance.variance(listofnumbers)
    def standarddeviation(self, listofnumbers):
        return StandardDeviation.StandDev(listofnumbers)
