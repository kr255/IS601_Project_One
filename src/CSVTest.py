import unittest
from ReaderOfCSVs import ReaderOfCSVs


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        path = r'src/UnitTestAddition.csv'
        self.csvReader = ReaderOfCSVs(path)




if __name__ == '__main__':
    unittest.main()
