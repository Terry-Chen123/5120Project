import django
django.setup()
from django.shortcuts import render
from Vaccine.models import Vaccine_option
import json

def test(request):
    recommendation = Vaccine_option.objects.all().values()
    l = []
    dic = {}
    for i in recommendation:
        l.append(i)
    dic['list'] = l
    context = {"recommendation": json.dumps(dic)}
    return render(request,'../templates/test_vaccine.html', context)

def recommend(request):
    ans = request.session['Q1'] + request.session['Q2'] + request.session['Q3']
    context = {'service_cache':ans}
    return render(request, '../templates/vaccine_recommendation.html', context)
