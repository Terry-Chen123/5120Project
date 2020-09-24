import random
import django
django.setup()
from Quiz.models import Question,Category, Clinic
import re

def generateRandomNum():
    list = []
    for i in range(1,6):
        list.append(i)
    slice = random.sample(list, 3)  # 从list中随机获取5个元素，作为一个片断返回
    return slice

def searchArea(input, choose, type):
    pattern = re.compile(input.lower())
    #get all clinic
    hospitals = Clinic.objects.all()
    search_result = []
    result_remind = ''
    for hospital in hospitals:
        if choose == 'Clinic Name':
            hospital_str = hospital.clinic_name
        elif choose == 'Clinic Location':
            hospital_str = hospital.suburb
        else:
            hospital_str = hospital.clinic_name + hospital.address
        m = pattern.search(hospital_str.lower())
        if m == None:
            result_remind += 'No Hospital found, try to search again'
        else :
            search_result.append(hospital)

    if type != 'All Clinic Type':
        temp = []
        for result in search_result:
            if result.clinic_type == type:
                temp.append(result)
        search_result = temp

    num = len(search_result)
    result_remind = 'There are ' + str(num) + ' related results found'
    return search_result, result_remind, num

#sort the clinic by rating
def sortRating(clinic_list):
    sort_list = list(clinic_list)
    sort_list.sort(key=lambda x:x.rating,reverse=True)
    return sort_list

