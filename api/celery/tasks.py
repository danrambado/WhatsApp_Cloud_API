import time
from app import celery

@celery.task
def add(x: int, y: int) -> int:
    time.sleep(5)
    return x + y
