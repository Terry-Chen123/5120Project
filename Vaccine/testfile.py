import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()
import json
from django.shortcuts import render
from Vaccine.models import Vaccine_option
from django.http import JsonResponse
from django.core import serializers

recommendation = Vaccine_option.objects.all().values()
r = Vaccine_option.objects.all().values_list()
l = []
dic = {}
#print(r)
#print(recommendation)
for i in recommendation:
    l.append(i)
dic['list'] = l
print((str(dic)))