from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/items')
def get_items():
    items = [{"id": 1, "name": "Item One"}, {"id": 2, "name": "Item Two"}]
    return jsonify(items)