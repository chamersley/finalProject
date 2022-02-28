# Generated by Django 4.0.2 on 2022-02-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profileLive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeIn', models.TimeField(auto_now=True)),
                ('timeOut', models.TimeField(auto_now=True)),
                ('vacationUsed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vacationInput', models.BooleanField(default=False)),
                ('sickUsed', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sickInput', models.BooleanField(default=False)),
                ('yearsExperience', models.IntegerField()),
            ],
        ),
    ]