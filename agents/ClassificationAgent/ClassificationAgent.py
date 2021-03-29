import requests
import json
import sys

settings = {
        'Classificator': 'http://procagent.antispam-msu.site/classificator'
}

def classify():
    lines = ''.join(sys.stdin.readlines())

    letter = lines

    login = sys.argv[1]
    domain = sys.argv[2]
    email = login + '@' + domain

    req_data = {'email': email, 'letter':letter}
    response = requests.post(settings['Classificator'], json=req_data)

    with open('Output.txt', 'w') as f:
        f.write(login)
        f.write(domain)
        f.write(email)

        for item in lines:
            f.write("%s" % item)

        print(response.request.url)
        print(response.request.body.decode('utf-8'))
        print(response.request.headers)


    with open('responses.txt', 'w') as f:
        f.write(response.text)

    result = response.json()['result']
    score = letter_with_headers = response.json()['score']

    #for item in letter_with_headers:
    #    sys.stdout.write(item)

    sys.stdout.write(str(score)+ ' ' + result)

classify()
sys.exit(0)
              