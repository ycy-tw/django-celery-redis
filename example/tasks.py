from celery import shared_task
import time
import random


@shared_task
def add_five(x):
    return x + 5


@shared_task
def add_five_after_5_sec(x):
    time.sleep(5)
    return x + 5


@shared_task
def add_random(x):
    return x + random.random()
