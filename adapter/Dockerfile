FROM python:3.6

WORKDIR /adapter

COPY requirements.txt /adapter
RUN pip install -r requirements.txt

COPY adapter.py /adapter
CMD python adapter.py http://0.0.0.0:8000/admin
