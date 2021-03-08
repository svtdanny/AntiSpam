# AntiSpam
Antispam system for CMC faculty of Lomonosov Moscow State University

![Antispam architech (2)](https://user-images.githubusercontent.com/66482706/110344305-68d43f00-803e-11eb-9699-e0d9f6c7fdca.png)

Архитектура

## Почтовый сервер
Классифицирующий агент - python скрипт, запускается непосредственно procmail

## Сервер загрузки
Обучающий агент
flask-модуль; python-модуль, реализующий взаимодействие с IMAP; Потенциально - celery модуль для фонового выполнения
1. Получает запрос от пользовательского интерфейса, загружает данные по IMAP, отправляет Агенту-процессору
2. Потенциально: запуск загрузки писем в фоновом режиме через Celery

## Сервер процессор
Агент-процессор
flask-модуль; python-модуль, реализующий взаимодействие с IMAP; Потенциально - celery модуль для фонового выполнения

Получает письмо на классификацию. Предобрабатывает его. Отправляет в ответе Классифицирующему агенту
Получает массивы писем входящие/спам. Предобрабатывает. Обучает модель. Сохраняет модель
Потенциально: запуск обучения в фоновом режиме через Celery
		
## Сервер базы данных
MongoDB
Хранит информацию для пользовательского интерфейса
Потенциально: хранит дополнительную информацию для агентов

## Сервер пользовательского интерфейса
Vue.js - Визуальный интерфейс системы
django - Логика и обработка структур данных пользователей
Могут быть запущены на разных серверах

