# Generated by Django 4.2 on 2023-05-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0003_merge_20230521_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='approved_vacation_number',
        ),
        migrations.AddField(
            model_name='vacation',
            name='emp_Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]