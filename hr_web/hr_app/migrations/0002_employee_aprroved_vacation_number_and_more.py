# Generated by Django 4.2 on 2023-05-20 09:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='aprroved_vacation_number',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1, message='Value must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(10, message='Value must be less than or equal to 10.')]),
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='employee',
            name='vacation_number',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(1, message='Value must be greater than or equal to 1.'), django.core.validators.MaxValueValidator(10, message='Value must be less than or equal to 10.')]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(2000, message='Value must be greater than or equal to 2000.'), django.core.validators.MaxValueValidator(6000, message='Value must be less than or equal to 6000.')]),
        ),
    ]