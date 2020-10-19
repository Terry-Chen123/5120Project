import random
import django
django.setup()
from Quiz.models import Question,Category
import sqlite3

def generateRandomNum():
    list = []
    for i in range(1,6):
        list.append(i)
    slice = random.sample(list, 3)
    return slice

