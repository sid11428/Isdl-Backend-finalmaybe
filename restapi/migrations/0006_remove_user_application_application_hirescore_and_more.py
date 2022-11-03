# Generated by Django 4.1.2 on 2022-11-02 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_remove_job_phd_req_remove_user_hum_acess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='application',
        ),
        migrations.AddField(
            model_name='application',
            name='hireScore',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restapi.job'),
        ),
        migrations.AlterField(
            model_name='application',
            name='spez_Req',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='restapi.spez'),
        ),
    ]