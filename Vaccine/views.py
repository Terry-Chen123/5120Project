import django
django.setup()
from django.shortcuts import render
from Vaccine.models import Vaccine_recommend
import json

def vaccine(request):
    recommendation_new = Vaccine_recommend.objects.all().values()
    l_new = []
    dic_new = {}
    for j in recommendation_new:
        l_new.append(j)
    dic_new['list'] = l_new

    context = {"recommendation_new": json.dumps(dic_new)}
    return render(request,'../templates/test_vaccine.html', context)


def prevention(request):
    return render(request, '../templates/prevention.html')

def health_habit(request):
    return render(request, '../templates/health_habit.html')

def airquality(request):
    return render(request, '../templates/air_quality.html')

