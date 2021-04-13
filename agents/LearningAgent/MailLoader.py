import imaplib
import getpass
from email.header import decode_header, make_header
from email import message_from_bytes, message
# Проблема с email. часто не видит свои же модули и функции! Решается прямой загрузкой соответствующих функций

import json

class ImapConnector:
    def __init__(self, imap_server, save_file=None):
        self.imap_server = imap_server
        self.imap = imaplib.IMAP4_SSL(imap_server)
        self.save_file = save_file

    def connect(self, email_address, password):
        if password:
            self.imap.login(email_address, password)
        else:
            # !!!Только для тестирования модуля. В конечном варианте должно быть убрано
            self.imap.login(email_address, getpass.getpass())

    def disconnect(self):
        self.imap.logout()

    @staticmethod
    def get_foldel_name(imap_list, general_name):
        result = []
        
        for i in imap_list[1]:
            l = i.decode().split(' "/" ')
            if general_name in l[0] or general_name in l[1]:
                result.append((l[0], l[1]))
                
        return tuple(result)
    
    @staticmethod
    def read_body(msg):
        # Необходимо, чтобы функция не принимала заглушки наподобие b' ' за текст
        # Это не мешает обойти систему послав очень длинную заглушку. Но это маловероятно
        body_len = 0
        
	#Возможен случай, когда сообщение не будет содержать полезных значений
        body = None

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
        
        if body is not None:
            return body.decode('utf-8','ignore')
        else:
            return ""

    def read_folder(self, name, n_letters, from_date=None):
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

        post_ids = post_ids[-n_letters:]

        readed_letters = []
        for post_id in post_ids:
            status, letter = self.imap.fetch(post_id, '(RFC822)')

            readed_letters.append(letter[0][1])

        if self.save_file != None:
            self.save_to_file(readed_letters)
        else:
            return readed_letters

    def save_to_file(self, readed_letters):
        assert(self.save_file is not None, 'Save directory isn`t specified')

        with open(self.save_file, 'w') as fout:
            #indent=0 для читаемости вывода
            #json.dump(readed_letters, fout, indent=0)
            for r in readed_letters:
                fout.write(r.decode('utf-8'))

    def __del__(self):
        #self.disconnect()
        pass

# Module testing
# Not for production using
if __name__ == '__main__':
    c = ImapConnector('jaffar.cs.msu.su', save_file='loaded_letters.txt')
    c.connect('isd', password=None)
    c.read_folder('INBOX', 5)

