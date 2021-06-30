import csv


class ReaderOfCSVs:

    '''
    Constructor
    @:param filepath, empty list
    open a file path specified for reading a csv
    DictReader from csv reads and reads it as a dictionary per line
    for example: {Value1: 580, Value2: 459, Value3: 1039}
    until EOF
    Each row in the csvRow is then added to a list
    '''
    def __init__(self, filepapa, listForData=[]):
        self._data = listForData
        with open(filepapa) as textToRead:
            csvrow = csv.DictReader(textToRead, delimiter=",")
            for row in csvrow:
                self._data.append(row)


    '''
    @:param classname
    '''
    def return_data_objects(self, classname):
