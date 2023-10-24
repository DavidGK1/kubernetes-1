from flask import Flask, jsonify, request
from mysql.connector import connect



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/items')
def get_items():
    items = [{"id": 1, "name": "Item One"}, {"id": 2, "name": "Item Two"}]
    return jsonify(items)

def connect_db():
    return connect(host="localhost", user="root", password="meow", database="my_flask_app")

@app.route('/create_user', methods=['POST'])
def create_user():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (request.form['name'], request.form['email']))
    db.commit()
    db.close()
    return "User created"