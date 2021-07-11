FROM python:latest

ADD Calculator /src

#CMD [ "python", "./Calculator/CSVTest.py" ]
CMD [ "python", "./src/CalculatorTest.py" ]