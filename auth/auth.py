from flask import Flask, request, Response
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import re

app = Flask(__name__)

config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'Cloud1x2Bet'
}


class User:
    def __init__(self, user_id, username, hashed_password, email, creation_date, last_login):
        self.user_id = user_id
        self.username = username
        self.hashed_password = hashed_password
        self.email = email
        self.creation_date = creation_date
        self.last_login = last_login

    def key(self):
        return self.user_id

    def __hash__(self):
        return hash(self.key())

    def __eq__(self, other):
        if self.user_id == other.user_id:
            return True
        return False

    def __str__(self):
        res = ""
        res += "User(" + self.user_id + "," + self.username + "," + self.email + ")"
        return res

    def serialize(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'hashed_password': self.hashed_password,
            'email': self.email,
            'creation_date': self.creation_date,
            'last_login': self.last_login
        }


def valid_username(username):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    statement = "SELECT * FROM Users WHERE username = \"{}\";".format(username)
    cursor.execute(statement)
    records = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    if records:
        return False
    return True


def insert_new_user(username, password, email):
    hashed_password = generate_password_hash(password, 'sha256')

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    statement = "INSERT INTO Users (username, hashed_password, email) VALUES (\"{}\", \"{}\", \"{}\");".format(username, hashed_password, email)
    cursor.execute(statement)
    connection.commit()
    cursor.close()
    connection.close()


def update_last_login_time(user_id):
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    statement = "UPDATE Users SET last_login = \"{}\" WHERE id = {};".format(current_timestamp, user_id)
    cursor.execute(statement)
    connection.commit()
    cursor.close()
    connection.close()


def get_user_data(username):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    statement = "SELECT id, hashed_password, email, creation_date, last_login FROM Users WHERE username = \"{}\";".format(username)
    cursor.execute(statement)
    record = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()

    if record is None:
        return None
    else:
        user_id, hashed_password, email, creation_date, last_login = (record[0], record[1], record[2], record[3], record[4])
        user = User(user_id, username, hashed_password, email, creation_date, last_login)
        return user.serialize()


@app.route('/register', methods=['GET', 'POST'])
def register():
    params = request.get_json(silent=True)
    if not params:
        return Response(status=400)

    username = params.get('username')
    if not username:
        return Response(status=400)

    password = params.get('password')
    if not password:
        return Response(status=400)

    email = params.get('email')
    if not email:
        return Response(status=400)

    if not valid_username(username):
        return Response(status=400)
    elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        return Response(status=400)
    elif not re.match(r'[A-Za-z0-9]+', username):
        return Response(status=400)
    else:
        insert_new_user(username, password, email)
        return Response(status=200)


@app.route('/login', methods=['GET', 'POST'])
def login():
    params = request.get_json(silent=True)
    if not params:
        return Response(status=400)

    username = params.get('username')
    if not username:
        return Response(status=400)

    password = params.get('password')
    if not password:
        return Response(status=400)

    user_data = get_user_data(username)

    if user_data is not None and check_password_hash(user_data['hashed_password'], password):
        update_last_login_time(user_data['user_id'])
        return Response(status=200)
    else:
        return Response(status=400)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
