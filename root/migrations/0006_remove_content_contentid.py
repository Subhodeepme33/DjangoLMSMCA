# Generated by Django 3.1 on 2020-09-09 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0005_users_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='contentid',
        ),
    ]
