# Generated by Django 3.2.9 on 2022-01-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_timesheetreport_project'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='dailytimesheet',
            constraint=models.UniqueConstraint(fields=('date', 'employee'), name='timesheet_dailytimesheet_unq__date__employee'),
        ),
    ]
