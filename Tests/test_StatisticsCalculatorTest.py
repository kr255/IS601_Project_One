import threading
import unittest
import logging
import pathlib
import sys
import unittest

from Statistics.StatisticsCalculator import StatisticsCalculator

print(sys.path)
from Calculator import Calculator
from CsvReader import ReaderOfCSVs

# from SquareRoot import squareRoot

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
        self.listofnum = [3,2,1,0,7,6,8,2]
        #self.emptyList = [1]

    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_stat_calc_mean(self):
        self.assertAlmostEqual(self.statCal.mean(self.listofnum), 3.625)

    def test_instantiate_stats_calculator(self):
        self.assertIsInstance(self.statCal, StatisticsCalculator)

if __name__ == '__main__':
    unittest.main()
