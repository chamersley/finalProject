from django.db import models
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import User

class account(models.Model):

    empFirst = models.CharField(max_length=255)
    empMiddle = models.CharField(max_length=255)
    empLast = models.CharField(max_length=255)
    empAddress = models.CharField(max_length=255)
    empCity = models.CharField(max_length=255)
    empState = models.CharField(max_length=255)
    empZip = models.IntegerField(max_length=5)
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    empPhone = models.IntegerField(validators=[phoneRegex], max_length=17, blank=True)

class createAccount(User, models.Model):
    SALARYCHOICE = [
        'Yes', 'No'
    ]

    GENDERCHOICE = [
        ('Male', 'Female')
    ]

    User = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=GENDERCHOICE)
    startDate = models.DateField(max_length=8)
    idNumber = models.IntegerField(max_length=16)
    areSalary = forms.ChoiceField(choices=SALARYCHOICE, widget=forms.RadioSelect)

    if areSalary == 'No':
        wage = models.DecimalField(max_digits=5, decimal_places=2)
    else:
        salary = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.User.username

