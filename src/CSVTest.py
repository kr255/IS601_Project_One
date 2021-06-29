import unittest
from ReaderOfCSVs import ReaderOfCSVs


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        path = r'src/UnitTestAddition.csv'
        self.csvReader = ReaderOfCSVs(path)

    def test_something(self):
        self.assertEqual(True, True)



if __name__ == '__main__':
    unittest.main()
