import django
django.setup()
from Search.models import Clinic
from django.shortcuts import render
from .otherFunction import searchArea, sortRating
import json

def searchClinic(request):

    hospital_all = Clinic.objects.all()
    sort_hospital = sortRating(hospital_all)

    search_result_num = -1
    search_result = ''
    result_remind = ''
    result_divide = []
    type = "22222222"
    choose = '222'
    if request.POST :
        #search keyword
        keyword = request.POST.get('searchclinic')
        #search base on which type
        type = request.POST.get('choose-type')
        #name or location
        choose = request.POST.get('getChoose')
        #get the search result and number of result
        search_result, result_remind, search_result_num = searchArea(keyword,choose,type)
        i = 0
        temp=[]
        #sort the search by rating
        sort_search_result = sortRating(search_result)
        #divide the result by 2 of each, because each line have 2 results
        while i < len(sort_search_result):
            if i % 2 !=0:
                temp.append(sort_search_result[i])
                i+=1
            else:
                temp = []
                temp.append(sort_search_result[i])
                i+=1
            if (i+1)%2 == 0:
                result_divide.append(temp)
    else:
        result = 'Search Error'

    clinic_all = Clinic.objects.all().values()
    l_new = []
    dic_new = {}
    for j in clinic_all:
        l_new.append(j)
    dic_new['list'] = l_new

    context = {'recommendhospital': sort_hospital[:5],
               'search_result_num': search_result_num,
               'search_result': search_result,
               'result_remind': result_remind,
               'result_divide': result_divide,
               'choose': choose,
               }

    return render(request, "../templates/search.html",context)

def searchResult(request):
    hospital_all = Clinic.objects.all()
    if request.POST :
        for i in range(len(hospital_all)):
            if str(i) in request.POST:
                hospital = Clinic.objects.get(id=i)
    else:
        result = 'Search Error'
    context = {'hospital':hospital}
    return render(request, "../templates/search_result.html", context )