from django.db import models
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import AbstractBaseUser
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

class createAccount(AbstractBaseUser, models.Model):
    SALARYCHOICE = [
        'Yes', 'No'
    ]

    GENDERCHOICE = [
        ('Male', 'Female')
    ]

    user = models.OneToOneField(AbstractBaseUser, null=True, on_delete=models.CASCADE)
    related = models.ForeignKey()
    DOB = models.DateTimeField()
    gender = models.CharField(max_length=6, choices=GENDERCHOICE)
    startDate = models.DateField(max_length=8)
    idNumber = models.IntegerField()
    areSalary = forms.ChoiceField(choices=SALARYCHOICE, widget=forms.RadioSelect)
    vacationTotal = models.DecimalField(max_digits=5, decimal_places=2)
    sickTotal = models.DecimalField(max_digits=5, decimal_places=2)

    USERNAME_FIELD = 'user'

    if areSalary == 'No':
        wage = models.DecimalField(max_digits=5, decimal_places=2)
    else:
        salary = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return self.User.username

