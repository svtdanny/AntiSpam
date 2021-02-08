import requests 
import json
import sys

settings = {
    'Classificator': 'localhost/classificator',
}

def classify():
    lines = sys.stdin.readlines()
    letter = json.loads(lines[0])

    login = sys.argv[1]
    domain = sys.argv[2]
    email = login + '@' + domain

    req_data = {'email': email, 'letter':letter} 
    response = requests.post(settings['Classificator'], req_data)

    letter_with_headers = response['result']

    sys.stdout.write(letter_with_headers)

if __name__ == '__main__':
    classify()