FROM python:latest

ADD src /src

CMD [ "python", "./src/CSVTest.py" ]