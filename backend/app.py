from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/guestbook'
mongo = PyMongo(app)

class Message:
    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = mongo.db.messages.find()
    result = []
    for message in messages:
        result.append({'name': message['name'], 'comment': message['comment']})
    return jsonify(result)

@app.route('/messages', methods=['POST'])
def add_message():
    name = request.json.get('name', '')
    comment = request.json.get('comment', '')
    
    if name and comment:
        new_message = {'name': name, 'comment': comment}
        mongo.db.messages.insert_one(new_message)
        return jsonify({'message': 'Message added successfully'}), 201
    else:
        return jsonify({'error': 'Name and comment are required'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

