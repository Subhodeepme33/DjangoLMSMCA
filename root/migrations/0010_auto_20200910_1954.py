# Generated by Django 3.1 on 2020-09-10 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_course_coursecategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='courseuid',
        ),
        migrations.AddField(
            model_name='subscription',
            name='courseid',
            field=models.IntegerField(default=None),
        ),
    ]
