FROM python:latest

ADD src /src

CMD [ "python", "./src/CalculatorTest.py" ]