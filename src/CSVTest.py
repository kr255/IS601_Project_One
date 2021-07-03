import unittest
from ReaderOfCSVs import ReaderOfCSVs, classfactory
import logging
import sys

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
        path = r'src/UnitTestAddition.csv'
        stream_handler.stream = sys.stdout
        self.csvReader = ReaderOfCSVs(path)

    '''
    addition = self.csvReader.create_class_dynamically("addition")
    creates a list of objects as [('addition', (objects,), dictionary), ...]
    self.assertIsInstance checks to see if its of type List

    '''
    def test_return_data_as_objs(self):
        addition = self.csvReader.create_class_dynamically("addition")
        self.assertIsInstance(addition, list)
        print(addition[0])
        test_class = classfactory('addition', self.csvReader.data[0])
        for add in addition:
            #print(add.__bases__)
            self.assertEqual(add.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
