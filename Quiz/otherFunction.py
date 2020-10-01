import random
import django
django.setup()
from Quiz.models import Question,Category
import sqlite3

def generateRandomNum():
    list = []
    for i in range(1,6):
        list.append(i)
    slice = random.sample(list, 3)  # 从list中随机获取5个元素，作为一个片断返回
    return slice

