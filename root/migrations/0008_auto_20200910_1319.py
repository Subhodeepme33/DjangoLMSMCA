# Generated by Django 3.1 on 2020-09-10 07:49

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_auto_20200909_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='contenturl',
            field=embed_video.fields.EmbedVideoField(),
        ),
    ]