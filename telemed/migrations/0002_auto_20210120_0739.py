# Generated by Django 3.1.5 on 2021-01-19 23:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='physician',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='prof_pics/'),
        ),
        migrations.AlterField(
            model_name='consultationrecord',
            name='consultation_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 20, 7, 39, 33, 20855), null=True),
        ),
        migrations.AlterField(
            model_name='consultationrecord',
            name='consultation_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 1, 20, 7, 39, 33, 20855), null=True),
        ),
    ]
