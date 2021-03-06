import email
from email import message
import sys
import joblib
from bs4 import BeautifulSoup
import sklearn
import nltk
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import re
from sklearn.svm import SVC
from bs4 import Comment
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
import pymorphy2

nltk.download('stopwords')

class Classificator():
    def __init__(self, email):
        self.email = email
        self.n_features = 10000 #Уменьшай если работает долго

    @staticmethod
    def dummy(data):
        return data

    @staticmethod
    def tokenize_and_lemmatize(raw_text):
        regex = re.compile('[^а-яА-Я ]') #Возможна ошибка кодировки
        raw_text = regex.sub(' ', raw_text)
        tokens = nltk.word_tokenize(raw_text.lower())
        stop_words = stopwords.words('russian')
        lemmatizer = pymorphy2.MorphAnalyzer()
        tokens = [lemmatizer.parse(word)[0].normal_form for word in tokens if word not in stop_words]     
        return tokens

    def fit(self, X, y):
        """
        X - list of vectors; prepared letters
        is_spam - int [-1,1]
        """
        self.vectorizer = TfidfVectorizer(use_idf = False, tokenizer=Classificator.tokenize_and_lemmatize, preprocessor=Classificator.dummy)
        self.model = SVC(probability=True, max_iter=5000) #Уменьшай если работает долго
        train_X = self.vectorizer.fit_transform(X).toarray()
        self.selector = SelectKBest(chi2, k=min(self.n_features, len(train_X[0])))
        train_X = self.selector.fit_transform(train_X, y)
        self.model.fit(train_X, y)
        joblib.dump([self.model, self.vectorizer, self.selector], '/home/antispam/agents/ProcessorAgent/models/'+self.email)

    def predict(self, prep_msg):
        """
        return: 
        result - str  'YES'/'NO'
        score - float [0...]; Bigger score = bigger probability of spam
        """
        try:
            self.model, self.vectorizer, self.selector = joblib.load('models/'+self.email)
        except:
            raise Exception('model doesn\'t exist yet')

        test_X = self.selector.transform(self.vectorizer.transform(prep_msg).toarray())
        result = self.model.predict(test_X)[0]
        #!!! Если для спама выдает скор <0.5 то поменяй 1 на 0
        score = self.model.predict_proba(test_X)[0][1] 
        if result == 1:
            return "YES", score
        else:
            return 'NO', score
    
    @staticmethod
    def tag_visible(element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]'] or isinstance(element, Comment):
            return False
        else:
            return True

    @staticmethod
    def process_html(txt):
        soup = BeautifulSoup(txt, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(Classificator.tag_visible, texts)
        return ' '.join(visible_texts) 

    #Возможна ошибка код
    @staticmethod
    def process_part(part):
        if part.get_content_type() == 'text/':
            return part.get_payload(decode=True).decode()
        if part.get_content_maintype() == "text" or part.get_content_maintype() == "plain":
            txt = part.get_payload(decode=True).decode()
            if bool(BeautifulSoup(txt, "html.parser").find()):
                return Classificator.process_html(txt)
            elif part.get_content_subtype() == 'plain' or part.get_content_subtype() == 'enriched' or part.get_content_subtype() == 'text':
                return txt
            else:
                return ''
        else:
            return ''

    @staticmethod
    def process_email(msg):
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

    @staticmethod
    def prepare_data(msgs_list):
        # Здесь необходимо использовать модуль DataPreparator
        # Метод создан для сохранения интерфейса
        texts = []
        for msg in msgs_list:
            # В документации написано про байтовое представление. Однако через stdin передаются строки (str). 
            # Быть осторожным!
            # msg = email.message_from_bytes(letter, _class = email.message.EmailMessage)
            decoded_msg = email.message_from_string(msg, _class = email.message.EmailMessage)

            texts.append(Classificator.process_email(decoded_msg))
        return texts

# Не обязательной умещать все в одном файле, однако он достаточно мал
if __name__ == "__main__":
    # В документации указано, что письмо подается на стандартный вход (stdin) и отфильтрованное письмо возвращается на stdout
    msg = sys.stdin.read()

    modeler = Classificator('test@cs.msu.ru')
    filtered_msg = modeler.predict(msg)

    sys.stdout.write(filtered_msg)
    
