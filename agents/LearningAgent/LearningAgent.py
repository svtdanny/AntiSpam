import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from MailLoader import ImapConnector
import requests

import json

app = Flask(__name__)
api = Api(app)

settings = {
    'imap_server': 'imap.gmail.com',
    'ProcessorAgent': 'http://procagent.antispam-msu.site/fit-model',
}

@app.route('/', methods=['GET'])
def hello():
    return 'Servise is working! It`s learning agent. CMC MSU Antispam'

def send_to_processor(email, inbox, spam):
        req_data = {
            'email': email,
            'inbox': inbox,
            'spam': spam
            } 
                    
        response = requests.post(settings['ProcessorAgent'], json=req_data)

        return response.status_code

class CreateModel(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        #Либо надо делать суперюзера, либо вводить пароль снова
        email = data['email']
        password = data['password']
        inbox_volume = data['inbox_volume']
        spam_volume = data['spam_volume']

        loader = ImapConnector(settings['imap_server'])
        loader.connect(email, password)
        
        inbox = loader.read_folder('INBOX', inbox_volume)
        spam = loader.read_folder('Junk', spam_volume)

        with open('/home/antispam/AntiSpam/agents/LearningAgent/loaded_inbox.txt', 'w') as f:
            #indent=0 для читаемости вывода
            #json.dump(inbox, f, indent=0)
            for r in inbox:
                f.write(r.decode('utf-8'))

        with open('/home/antispam/AntiSpam/agents/LearningAgent/loaded_spam.txt', 'w') as f:
            #indent=0 для читаемости вывода
            #json.dump(spam, f, indent=0)
            for r in spam:
                f.write(r.decode('utf-8'))
        
        send_to_processor(email, inbox, spam)

api.add_resource(CreateModel, '/create-model')

"""
curl -X POST -H "Content-Type: application/json" -d '{"email": "sivtsovdt@gmail.com", "password": "", "inbox_volume": 10, "spam_volume": 10}' http://learnagent.antispam-msu.site/create-model
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
