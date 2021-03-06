import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import email

from Classificator import Classificator

import json


app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def hello():
    return 'Servise is working! It`s processor agent. CMC MSU Antispam'

class FitModel(Resource):
    @staticmethod
    def post():
        data = request.get_json()
        
        email = data['email']
        inbox = data['inbox']
        spam = data['spam']

        inbox_prep = Classificator.prepare_data(inbox)
        spam_prep = Classificator.prepare_data(spam)

        y_inbox = [-1 for el in inbox_prep]
        y_spam = [1 for el in spam_prep]
        
        X = inbox_prep + spam_prep
        y = y_inbox + y_spam

        cl = Classificator(email)
        cl.fit(X, y)

        return jsonify({})

class SpamEvaluator(Resource):
    @staticmethod
    def post():
        data = request.get_json()

        with open('/home/antispam/agents/ProcessorAgent/Output.txt', 'a') as f:
            f.write(json.dumps(data))

        email_addr = data['email']
        letter = data['letter']



        cl = Classificator(email_addr)
        prep_msg = Classificator.prepare_data([letter])
        result, score = cl.predict(prep_msg)

        msg['AntiSpam-Result'] = str(result)
        msg['AntiSpam-Score'] = str(score)

        # return jsonify({'result': msg.as_bytes()})
        return jsonify({'result': msg.as_string()})

api.add_resource(FitModel, '/fit-model')
api.add_resource(SpamEvaluator, '/classificator')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)