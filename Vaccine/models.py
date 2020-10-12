from django.db import models

# Create your models here.
class Vaccine_option(models.Model):

    choice = models.CharField(max_length=1000)
    recommendation = models.CharField(max_length=1000)