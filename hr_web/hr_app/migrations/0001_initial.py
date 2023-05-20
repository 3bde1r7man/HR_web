# Generated by Django 4.2.1 on 2023-05-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=50)),
                ('material_status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('widowed', 'widowed'), ('divorced', 'divorced'), ('separated', 'separated')], max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('phone', models.IntegerField()),
                ('vcation_days', models.IntegerField()),
                ('approved_vacation', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]