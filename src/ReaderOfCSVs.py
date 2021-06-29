import csv


class ReaderOfCSVs:
    #empty list to store dic val from the csv

    '''constructor
    Creates a new instance of ReaderOfCSVs
    open a file path specified as text for reading
    DictReader from csv reads and reads it as a dictionary per line
    for example: {Value1: 580, Value2: 459, Value3: 1039}
    until EOF
    Each row in the csvRow is then added to _data[] list
    '''
    def __init__(self, filepapa):
        self._data = []
        with open(filepapa) as textToRead:
            csvrow = csv.DictReader(textToRead)
            for row in csvrow:
                self._data.append(row)

