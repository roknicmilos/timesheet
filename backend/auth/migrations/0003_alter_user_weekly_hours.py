# Generated by Django 3.2.9 on 2021-12-25 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet_auth', '0002_auto_20211225_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='weekly_hours',
            field=models.FloatField(default=40, verbose_name='weekly hours'),
        ),
    ]
