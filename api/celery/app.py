from celery import Celery

app = Celery('tasks', BROKER_URL = 'redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y
