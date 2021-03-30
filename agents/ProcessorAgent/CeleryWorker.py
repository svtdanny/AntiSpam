from celery import Celery 
from Classificator import Classificator

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def delay_fit(model, X, y):
    model.fit(X, y)
