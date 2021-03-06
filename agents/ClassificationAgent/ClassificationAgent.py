import requests 
import json
import sys

settings = {
        'Classificator': 'http://procagent.antispam-msu.site/classificator'
}

def classify():
    lines = sys.stdin.readlines()
    
    letter = lines

    login = sys.argv[1]
    domain = sys.argv[2]
    email = login + '@' + domain
    
    with open('/home/antispam/agents/ClassificationAgent/Output.txt', 'w') as f:
        f.write(login)
        f.write(domain)
        f.write(email)

        for item in lines:
            f.write("%s" % item)


    req_data = {'email': email, 'letter':letter} 
    response = requests.post(settings['Classificator'], json=req_data)

    with open('/home/antispam/agents/ClassificationAgent/responses.txt', 'w') as f:
        f.write(response.text)


    letter_with_headers = response['result']

    sys.stdout.write(letter_with_headers)


classify()
