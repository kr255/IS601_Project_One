FROM python:latest
ADD . /src


ENV PYTHONPATH "${PYTHONPATH}:/src/Calculator:/src/CsvReader:/src/Tests:/src/Operations:/src/Statistics:/src"
#CMD [ "python", "./Calculator/test_CSVTest.py" ]
CMD [ "python", "/src/Tests/test_StatisticsCalculatorTest.py" ]
#CMD [ "python", "/src/Statistics/StatisticsCalculator.py" ]