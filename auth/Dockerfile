FROM python:3.6

EXPOSE 5000

WORKDIR /auth

COPY requirements.txt /auth
RUN pip install -r requirements.txt

COPY auth.py /auth
CMD python auth.py
