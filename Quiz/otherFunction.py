import random
import django
django.setup()
from Quiz.models import Question,Category, Hospital1
import re

def generateRandomNum():
    list = []
    for i in range(1,6):
        list.append(i)
    slice = random.sample(list, 3)  # 从list中随机获取5个元素，作为一个片断返回
    return slice

def searchArea(input):
    pattern = re.compile(input.lower())
    hospitals = Hospital1.objects.all()
    search_result = []
    result_remind = ''
    for hospital in hospitals:
        #hospital_str = hospital.hospital_name + ' ' + hospital.roadName + ' ' + \
        #hospital.area + ' ' + str(hospital.postcode) + ' ' + hospital.state
        hospital_str = hospital.hospital_name
        m = pattern.search(hospital_str.lower())
        if m == None:
            result_remind += 'No Hospital found, try to search again'
        else :
            search_result.append(hospital)
    num = len(search_result)
    result_remind = 'There are ' + str(num) + ' related results found'
    return search_result, result_remind, num



temp=[]
i=0
result_divide = []
search_result=[1]
while i < len(search_result):
    if i % 2 !=0:
        temp.append(search_result[i])
        i+=1
    else:
        temp = []
        temp.append(search_result[i])
        i+=1
    if (i+1)%2 == 0:
        result_divide.append(temp)
print(result_divide)