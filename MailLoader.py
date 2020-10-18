import imaplib
import getpass
from email.header import decode_header, make_header
from email import message_from_bytes, message
# Проблема с email. часто не видит свои же модули и функции! Решается прямой загрузкой соответствующих функций

import json

class ImapConnector:
    def __init__(self, imap_server, email_address, password=None, save_file=None):
        self.imap_server = imap_server
        self.imap = imaplib.IMAP4_SSL(imap_server)
        self.save_file = save_file

        if password:
            self.imap.login(email_address, email_address)
        else:
            # !!!Только для тестирования модуля. В конечном варианте должно быть убрано
            self.imap.login(email_address, getpass.getpass())

    @staticmethod
    def get_foldel_name(imap_list, general_name):
        result = []
        
        for i in imap_list[1]:
            l = i.decode().split(' "/" ')
            if general_name in l[0]:
                result.append((l[0], l[1]))
                
        return tuple(result)
    
    @staticmethod
    def read_body(msg):
        # Необходимо, чтобы функция не принимала заглушки наподобие b' ' за текст
        # Это не мешает обойти систему послав очень длинную заглушку. Но это маловероятно
        body_len = 0
        
        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()
                cdispo = str(part.get('Content-Disposition'))

                # Пропустить любые text/plain (txt) вложения
                if ctype == 'text/plain' and 'attachment' not in cdispo:
                    if body_len < len(part.get_payload(decode=True)):
                        body = part.get_payload(decode=True)  # decode
                        body_len = len(body)
            # Письмо без деления на части. plain text без вложений. !Не дает гарантии, что это будет именно текст
            # может быть только вложение
        else:
            body = msg.get_payload(decode=True)
            
        return body.decode('utf-8','ignore')

    def read_folder(self, name, from_date=None):
        imap_list = self.imap.list(pattern='*')
        folders = ImapConnector.get_foldel_name(imap_list, name)

        assert(len(folders) != 0), 'Folder doesn`t exist'
        assert(len(folders) == 1), 'To much folder for the name (>1)'

        self.imap.select(folders[0][1])
        if from_date:
            # date format: dd-Mnth-yyyy (01-Jan-2020)
            resp, ids = self.imap.search(None, '(SINCE "', from_date,'")')
        else:
            resp, ids = self.imap.search(None, 'ALL')
        
        post_ids = ids[0].decode().split(' ')
        post_ids = [p_id.encode() for p_id in post_ids]

        readed_letters = []
        for post_id in post_ids:
            status, letter = self.imap.fetch(post_id, '(RFC822)')

            msg = message_from_bytes(letter[0][1], _class = message.EmailMessage)
            parsed_letter = dict(msg)

            for key in parsed_letter.keys():
                parsed_letter[key] = str(make_header(decode_header(parsed_letter[key])))

            body = ImapConnector.read_body(msg)
            parsed_letter['Body'] = body

            readed_letters.append(parsed_letter)

        if self.save_file != None:
            self.save_to_file(readed_letters)
        else:
            raise Exception('Errror: ', 'No one of saving ways was used! Check parameters for file savings')

    def save_to_file(self, readed_letters):
        assert(self.save_file is not None, 'Save directory isn`t specified')

        with open(self.save_file, 'w') as fout:
            #indent=0 для читаемости вывода
            json.dump(readed_letters, fout, indent=0)

        
# Module testing
# Not for production using
if __name__ == '__main__':
    c = ImapConnector('imap.gmail.com', 'widosmile@gmail.com', password=None, save_file='loaded_letters.txt')
    c.read_folder('Junk')
