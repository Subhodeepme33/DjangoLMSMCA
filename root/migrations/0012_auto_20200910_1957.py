# Generated by Django 3.1 on 2020-09-10 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0011_auto_20200910_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='useruid',
            new_name='userid',
        ),
    ]
