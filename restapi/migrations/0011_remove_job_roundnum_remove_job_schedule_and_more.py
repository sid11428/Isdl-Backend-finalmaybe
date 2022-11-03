# Generated by Django 4.1.2 on 2022-11-03 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0010_job_phd_req_job_roundnum_job_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='roundNum',
        ),
        migrations.RemoveField(
            model_name='job',
            name='schedule',
        ),
        migrations.AddField(
            model_name='application',
            name='roundNum',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
