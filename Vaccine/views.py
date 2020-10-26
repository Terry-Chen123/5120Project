import django
django.setup()
from django.shortcuts import render
from Vaccine.models import Vaccine_recommend
import json

def vaccine(request):
    #get all recommendation from database
    recommendation = Vaccine_recommend.objects.all().values()
    l = []
    dic = {}
    for j in recommendation:
        l.append(j)
    dic['list'] = l

    context = {"recommendation_new": json.dumps(dic)}
    return render(request, '../templates/vaccine.html', context)

def prevention(request):
    return render(request, '../templates/prevention.html')

def health_habit(request):
    return render(request, '../templates/health_habit.html')

def airquality(request):
    return render(request, '../templates/air_quality.html')

