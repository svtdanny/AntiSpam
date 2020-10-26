import email
from email import message
import sys

class ClassificationAgent():
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

    def predict(self, prep_msg):
        # Здесь необходимо использовать http или RPC, чтобы синхронно запросить результат у агента процессора
        # Будет реализована после определения интерфейса агента процессора
        return 'NO', 0

    def prepare(self, msg):
        # Здесь необходимо использовать модуль DataPreparator
        # Метод создан для сохранения интерфейса
        return msg

    def classify_email(self,letter):
        # В документации написано про байтовое представление. Однако через stdin передаются строки (str). 
        # Быть осторожным!
        # msg = email.message_from_bytes(letter, _class = email.message.EmailMessage)
        msg = email.message_from_string(letter, _class = email.message.EmailMessage)

        prep_msg = self.prepare(msg)
        result, score = self.predict(prep_msg)

        msg['AntiSpam-Result'] = str(result)
        msg['AntiSpam-Score'] = str(score)

        # return msg.as_bytes()
        return msg.as_string()

# Не обязательной умещать все в одном файле, однако он достаточно мал
if __name__ == "__main__":
    # В документации указано, что письмо подается на стандартный вход (stdin) и отфильтрованное письмо возвращается на stdout
    msg = sys.stdin.read()

    agent = ClassificationAgent('test', 'cs.msu.ru')
    filtered_msg = agent.classify_email(msg)

    sys.stdout.write(filtered_msg)
    