import requests 
import json
import sys

settings = {
        'Classificator': 'http://procagent.antispam-msu.site/classificator'
}

def classify():
    lines = ''.join(sys.stdin.readlines())
    
    letter = ''.join(lines)

    login = sys.argv[1]
    domain = sys.argv[2]
    email = login + '@' + domain
    
    req_data = {'email': email, 'letter':letter}
    response = requests.post(settings['Classificator'], json=req_data)
    
    with open('/home/antispam/agents/ClassificationAgent/Output.txt', 'w') as f:
        f.write(response.request.url)
        f.write(response.request.body.decode('utf-8'))
        f.write(str(response.request.headers))


        #for item in lines:
        #    f.write("%s" % item)
        
        #print(response.request.url)
        #print(response.request.body.decode('utf-8'))
        #print(response.request.headers)

    
    with open('/home/antispam/agents/ClassificationAgent/responses.txt', 'w') as f:
        f.write(response.text)

    result = response.json()['result']
    score = letter_with_headers = response.json()['score']

    #for item in letter_with_headers:
    #    sys.stdout.write(item)
    
    print(str(score)+ ' ' + result)

classify()
sys.exit(0)
