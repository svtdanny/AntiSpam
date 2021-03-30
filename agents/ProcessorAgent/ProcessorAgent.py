import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import email
from urllib.parse import urlparse, parse_qsl


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
        data = request.get_data().decode('utf-8')
        data = dict(parse_qsl(data))
        # change on code below if python agent + json
        # data = request.get_json()

        with open('/home/antispam/agents/ProcessorAgent/Output.txt', 'w') as f:
            f.write(json.dumps(data))

        email_addr = data['email']
        letter = data['letter']

       
        if (len(letter) != 0):
            cl = Classificator(email_addr)
            prep_text = Classificator.prepare_data([letter])[0]
            result, score = cl.predict(prep_text)
        else:
            result, score = "NO", 0


        # code if you need to return letter with headers
        #msg = Classificator.json_to_dict(', '.join(letter))
        #response = [letter[0]] + ['AntiSpam-Result: ' + result + '\n', 'AntiSpam-score: ' + str(score) + '\n'] + letter[1:]
        
        response = {}
        response['result'] = result
        response['score'] = score
        
        # return jsonify({'result': msg.as_bytes()})
        return jsonify(response)

api.add_resource(FitModel, '/fit-model')
api.add_resource(SpamEvaluator, '/classificator')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
