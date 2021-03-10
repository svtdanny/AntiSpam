from celery import Celery 

import requests
from MailLoader import ImapConnector

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

def send_to_processor(email, inbox, spam):
        req_data = {
            'email': email,
            'inbox': inbox,
            'spam': spam
            }

        response = requests.post(settings['ProcessorAgent'], json=req_data)

        return response.status_code

@app.task
def delay_load_send_letters(data, imap_server):
    #Либо надо делать суперюзера, либо вводить пароль снова
    email = data['email']
    password = data['password']
    inbox_volume = data['inbox_volume']
    spam_volume = data['spam_volume']

    loader = ImapConnector(imap_server)
    loader.connect(email, password)

    inbox = loader.read_folder('INBOX', inbox_volume)
    spam = loader.read_folder('Junk', spam_volume)

    with open('/home/antispam/agents/LearningAgent/loaded_inbox.txt', 'w') as f:
        #indent=0 для читаемости вывода
        #json.dump(inbox, f, indent=0)
        for r in inbox:
            f.write(r.decode('utf-8'))

    with open('/home/antispam/agents/LearningAgent/loaded_spam.txt', 'w') as f:
        #indent=0 для читаемости вывода
        #json.dump(spam, f, indent=0)
        for r in spam:
            f.write(r.decode('utf-8'))
    
    send_to_processor(email, inbox, spam)