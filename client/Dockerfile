FROM python:3.6

WORKDIR /client

COPY requirements.txt /client
RUN pip install -r requirements.txt

COPY client.py /client
CMD python client.py http://0.0.0.0:8000/admin http://0.0.0.0:8000/service http://0.0.0.0:8000/auth
