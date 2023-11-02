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

@app.route('/get_users', methods=['GET'])
def get_users():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    db.close()
    return str(users)



@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (request.form['name'], request.form['email'], user_id))
    db.commit()
    db.close()
    return f"User with ID {user_id} updated"


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    db.commit()
    db.close()
    return f"User with ID {user_id} deleted"