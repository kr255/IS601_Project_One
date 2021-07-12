import logging
import sys
import unittest

from CsvReader.ReaderOfCSVs import ReaderOfCSVs, classfactory

'''
get the logger
set it to debug level 
set steam to standard out
add handler to logger    
'''

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.pathAddition = r'Calculator/UnitTestAddition.csv'
        self.pathSubtraction = r'Calculator/UnitTestSubtraction.csv'
        self.pathDivision = r'Calculator/UnitTestDivision.csv'
        self.pathMultiplication = r'Calculator/UnitTestMultiplication.csv'
        stream_handler.stream = sys.stdout

    '''
    addition = self.csvReader.create_class_dynamically("addition")
    creates a list of objects as [('addition', (objects,), dictionary), ...]
    self.assertIsInstance checks to see if its of type List

    '''
    def test_return_data_as_objs(self):
        self.csvReaderAdd = ReaderOfCSVs(self.pathAddition)
        addition = self.csvReaderAdd.create_class_dynamically("addition")
        self.assertIsInstance(addition, list)
        test_class_addition = classfactory('addition', self.csvReaderAdd._newData[0])
        for add in addition:
            #print(add.__name__, "\t", add.__dict__['Value 1'], "\t", add.__dict__['Value 2'], "\t", add.__dict__['Result'])
            #print(sub.__dict__['Value 1'], "\t", sub.__dict__['Value 2'], "\t", sub.__dict__['Result'])
            self.assertEqual(add.__name__, test_class_addition.__name__)


if __name__ == '__main__':
    unittest.main()
