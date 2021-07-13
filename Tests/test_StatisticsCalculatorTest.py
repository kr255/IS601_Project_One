import logging
import pathlib
import sys
import unittest

from Statistics.StatisticsCalculator import StatisticsCalculator

print(sys.path)
from Calculator import Calculator
from CsvReader import ReaderOfCSVs

'''
setting up logger for checking out of obj
redirecting it to standard out??

result:::: well should of read the documentation
setUp() is called per test method call so 1 obj is created per test.

get the logger
set it to debug level 
set steam to standard out
add handler to logger    
'''

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
pathAddition = r'/src/Tests/Data/UnitTestAddition.csv'
pathSubtraction = r'/src/Tests/Data/UnitTestSubtraction.csv'
pathDivision = r'/src/Tests/Data/UnitTestDivision.csv'
pathMultiplication = r'/src/Tests/Data/UnitTestMultiplication.csv'
'''
Test class for Calculator.py
'''

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        stream_handler.stream = sys.stdout
        #sys.setrecursionlimit(10 ** 7)  # max depth of recursion
        sys.setrecursionlimit(1000000)  # max depth of recursion
        #threading.stack_size(2 ** 27)  # new thread will get stack of such size
        self.statCal = StatisticsCalculator()
        self.listofnum = [2,1,7,6,8,2,8,8]
        #self.emptyList = [1]

    # def test_something(self):
    #     self.assertEqual(True, False)
    def test_stat_calc_stddev(self):
        self.assertAlmostEqual(self.statCal.standarddeviation(self.listofnum), 3.0589447)

    def test_stat_calc_var(self):
        self.assertAlmostEqual(self.statCal.variance(self.listofnum), 9.3571429)

    def test_stat_calc_mode(self):
        self.assertAlmostEqual(self.statCal.mode(self.listofnum), 8)

    def test_stat_calc_median(self):
        self.assertAlmostEqual(self.statCal.median(self.listofnum), 6.5)

    def test_stat_calc_mean(self):
        self.assertAlmostEqual(self.statCal.mean(self.listofnum), 5.25)

    def test_instantiate_stats_calculator(self):
        self.assertIsInstance(self.statCal, StatisticsCalculator)

if __name__ == '__main__':
    unittest.main()
