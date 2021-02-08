import email
from email import message
import sys
import joblib

class Classificator():
    def __init__(self, email):
        self.email = email

    def fit(self, X, y):
        """
        X - list of vectors; prepared letters 
        is_spam - int [0,1]
        """
        self.model = SOMEMODEL().fit(X, y)
        joblib.dump(self.model, 'models/'+self.email)

    def predict(self, prep_msg):
        """
        return: 
        result - str  'YES'/'NO'
        score - float [0...]; Bigger score = bigger probability of spam
        """
        try:
            self.model = joblib.load('models/'+self.email)
        except:
            raise Exception('model wasn`t exists yet')
        
        result, score = self.model.predict(prep_msg)

        return 'NO', 0
        #return result, score

    @staticmethod
    def prepare_data(msg):
        # Здесь необходимо использовать модуль DataPreparator
        # Метод создан для сохранения интерфейса
        return msg

# Не обязательной умещать все в одном файле, однако он достаточно мал
if __name__ == "__main__":
    # В документации указано, что письмо подается на стандартный вход (stdin) и отфильтрованное письмо возвращается на stdout
    msg = sys.stdin.read()

    modeler = Classificator('test@cs.msu.ru')
    filtered_msg = modeler.predict(msg)

    sys.stdout.write(filtered_msg)
    