from django.db import models
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
from django.core.exceptions import ValidationError

def onlyint(value):
    if not value.isdigit():
        raise ValidationError('This field only accepts numbers.')

class ourAccount(models.Model):
    empFirst = models.CharField(max_length=255)
    empMiddle = models.CharField(max_length=255)
    empLast = models.CharField(max_length=255)
    empAddress = models.CharField(max_length=255)
    empCity = models.CharField(max_length=255)
    empState = models.CharField(max_length=255)
    empZip = models.IntegerField()
    phoneRegex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    empPhone = models.IntegerField(validators=[phoneRegex], blank=True)

class createAccount(models.Model):
    SALARYCHOICE = [
        'Yes', 'No'
    ]

    GENDERCHOICE = [
        ('Male', 'Female')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    DOB = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=GENDERCHOICE)
    startDate = models.DateField(max_length=8)
    idNumber = models.IntegerField()
    areSalary = forms.ChoiceField(choices=SALARYCHOICE, widget=forms.RadioSelect)
    vacationTotal = models.DecimalField(max_digits=5, decimal_places=2)
    sickTotal = models.DecimalField(max_digits=5, decimal_places=2)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []
    is_anonymous = False
    is_authenticated = True

    if areSalary == 'No':
        wage = models.DecimalField(max_digits=5, decimal_places=2)
    else:
        salary = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.User.username

