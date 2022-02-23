from django.db import models

# Create your models here.

class profileLive(models.Model):
    timeIn = models.TimeField(auto_now=True)
    timeOut = models.TimeField(auto_now=True)
    vacationUsed = models.DecimalField(max_digits=5, decimal_places=2)
    vacationInput = models.BooleanField(default=False)
    sickUsed = models.DecimalField(max_digits=5, decimal_places=2)
    sickInput = models.BooleanField(default=False)
    yearsExperience = models.IntegerField()