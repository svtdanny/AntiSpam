import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import email
from urllib.parse import urlparse, parse_qsl

import requests

from Classificator import Classificator

import json
from datetime import datetime 

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
        
        start_time = datetime.now() 

        inbox_prep = Classificator.prepare_data(inbox)
        spam_prep = Classificator.prepare_data(spam)

        y_inbox = [-1 for el in inbox_prep]
        y_spam = [1 for el in spam_prep]
        
        X = inbox_prep + spam_prep
        y = y_inbox + y_spam

        cl = Classificator(email)
        cl.fit(X, y)

        end_time = datetime.now() 
        delta = end_time - start_time
        delta = str(delta).split(':')[-1]
        s_ms = delta.split('.')
        delta = s_ms[0] + '.' + s_ms[1][:3] 

        res = requests.post('http://api.antispam-msu.site/rest-auth/login/', data={'username':'antispam', 'password':'spammustdie'})
        key = res.json()['key']

        data = {'username': email,
                'lastLearn': end_time.strftime("%b %d %Y %H:%M:%S"), 
                'totalTime': delta, 
                'VolumeInbox': len(y_inbox), 
                'VolumeSpam': len(y_spam)}
        
        res = requests.put('http://api.antispam-msu.site/profile/sys_last_learn/',
                headers={'Authorization': 'Token ' + key}, 
                data=data)
        
        return jsonify({})

class SpamEvaluator(Resource):
    @staticmethod
    def post():
        data = request.get_data().decode('utf-8')
        data = dict(parse_qsl(data))
        # change on code below if python agent + json
        # data = request.get_json()

        with open('/home/antispam/AntiSpam/agents/ProcessorAgent/Output.txt', 'w') as f:
            f.write(json.dumps(data))

        email_addr = data['email']
        letter = data['letter']
        

        res = requests.post('http://api.antispam-msu.site/rest-auth/login/', 
                data={'username':'antispam', 'password':'spammustdie'})
        key = res.json()['key']

        res = requests.get('http://api.antispam-msu.site/profile/sys_mail_lists/',
                headers={'Authorization': 'Token ' + key}, 
                data={'username': email_addr})
        mail_lists = res.json()

        if (len(letter) != 0):
            cl = Classificator(email_addr)
            prep_text = Classificator.prepare_data([letter])[0]
            result, score = cl.predict(prep_text)
        else:
            result, score = "NO", 0

        try:
            res = requests.post('http://api.antispam-msu.site/rest-auth/login/', 
                    data={'username':'antispam', 'password':'spammustdie'})
            key = res.json()['key']

            res = requests.get('http://api.antispam-msu.site/profile/sys_mail_lists/',
                    headers={'Authorization': 'Token ' + key}, 
                    data={'username': email_addr})
            mail_lists = res.json()


            for bl in mail_lists['blackList'].split(','):
                if bl in letter:
                    result, score = "YES", 1
                    print('SYS: BL LIST USED')
            for wh in mail_lists['whiteList'].split(','):
                if wh in letter:
                    result, score = "NO", 0
                    print('SYS: WH LIST USED')
        except:
            print('SYS: FAILED to load b&w lists')

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
