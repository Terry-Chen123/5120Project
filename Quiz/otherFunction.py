import random
import django
django.setup()
from Quiz.models import Question,Category, Hospital
import re

def generateRandomNum():
    list = []
    for i in range(1,6):
        list.append(i)
    slice = random.sample(list, 3)  # 从list中随机获取5个元素，作为一个片断返回
    return slice

def searchArea(input):
    pattern = re.compile(input.lower())
    hospitals = Hospital.objects.all()
    search_result = []
    result_remind = ''
    for hospital in hospitals:
        hospital_str = hospital.labelName + ' ' + hospital.roadName + ' ' + \
        hospital.area + ' ' + str(hospital.postcode) + ' ' + hospital.state_name
        m = pattern.search(hospital_str.lower())
        if m == None:
            result_remind += 'No Hospital found, try to search again'
        else :
            search_result.append(hospital)
    num = len(search_result)
    result_remind = 'There are ' + str(num) + ' related results found'
    return search_result, result_remind

searchArea('ROY')
