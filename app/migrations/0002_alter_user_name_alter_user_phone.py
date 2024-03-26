# Generated by Django 5.0.2 on 2024-03-24 11:17

import app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5, message='name shoulb be 5 character'), app.models.name_validator]),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^[0-9]{10}$')]),
        ),
    ]