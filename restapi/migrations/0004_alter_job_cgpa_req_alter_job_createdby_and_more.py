# Generated by Django 4.1.2 on 2022-11-02 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_application_job_remove_applicant_application_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='cgpa_Req',
            field=models.DecimalField(decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='createdby',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='dept_name',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='phd_Req',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='post',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
