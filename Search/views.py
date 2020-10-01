import django
django.setup()
from Search.models import Clinic
from django.shortcuts import render
from .otherFunction import searchArea, sortRating
import sqlite3
# Create your views here.
def test(request):
    return render(request,'../templates/test.html')

def searchClinic(request):
    hospital_all = Clinic.objects.all()
    sort_hospital = sortRating(hospital_all)
    hospital1 = sort_hospital[:2]
    hospital2 = sort_hospital[2:4]
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
    return render(request, "../templates/search.html",{'recommendhospital1':hospital1,
                                                       'recommendhospital2': hospital2,
                                                       'search_result_num':search_result_num,
                                                       'search_result':search_result,
                                                       'result_remind':result_remind,
                                                       'result_divide':result_divide,
                                                       'choose':choose})

def searchResult(request):
    hospital_all = Clinic.objects.all()
    if request.POST :
        for i in range(len(hospital_all)):
            if str(i) in request.POST:
                hospital = Clinic.objects.get(id=i)
    else:
        result = 'Search Error'
    return render(request, "../templates/search_result.html", {'hospital':hospital,})