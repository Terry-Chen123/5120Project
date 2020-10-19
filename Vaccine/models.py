from django.db import models

class Vaccine_option(models.Model):

    choice = models.CharField(max_length=1000)
    recommendation = models.CharField(max_length=1000)

class Vaccine_recommend(models.Model):

    choice = models.CharField(max_length=1000)
    prevenar_13_total_dose = models.IntegerField()
    prevenar_13_remaining_dose = models.IntegerField()
    prevenar_13_detail_plan = models.CharField(max_length=1000)
    pneumovax_23_remaining_dose = models.IntegerField()
    pneumovax_23_detail_plan = models.CharField(max_length=1000)
    special_conditon = models.CharField(max_length=1000)
