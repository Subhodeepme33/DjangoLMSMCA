# Generated by Django 3.1 on 2020-09-23 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0020_auto_20200921_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='useractive',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='course',
            name='createdat',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 23, 21, 59, 20, 444010)),
        ),
    ]