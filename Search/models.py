from django.db import models

# Create your models here.
class Clinic(models.Model):

    clinic_name = models.CharField(max_length=500)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    longitude = models.DecimalField(max_digits=13, decimal_places=10)
    latitude = models.DecimalField(max_digits=13, decimal_places=10)
    clinic_type = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    suburb = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    website = models.CharField(max_length=500)