import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from MailLoader import ImapConnector

import requests 

app = Flask(__name__)
api = Api(app)

settings = {
    'imap_server': 'imap.gmail.com',
    'ProcessorAgent': 'localhost/fit',
    'PrepareService': 'localhost/prepare'
}

@app.route('/', methods=['GET'])
def hello():
    return 'Servise is working! It`s learning agent. CMC MSU Antispam'

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
        
        inbox = loader.read_folder('Inbox')[:-inbox_volume]
        spam = loader.read_folder('Junk')[:-spam_volume]

        inbox_prep = CreateModel.prepare_data(inbox)
        spam_prep = CreateModel.prepare_data(spam)
        
        CreateModel.send_to_processor(email, inbox, spam)

    @staticmethod
    def prepare_data(emails):
        req_data = {'emails':emails} 
        response = request.post(settings['PrepareService'])

        return response.json()['emails']

    @staticmethod
    def send_to_processor(email, inbox, spam):
        req_data = {
            'email': email,
            'inbox': inbox,
            'spam': spam
            } 
                    
        response = request.post(settings['ProcessorAgent'], req_data)

        return response.status_code

api.add_resource(CreateModel, '/create-model')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)