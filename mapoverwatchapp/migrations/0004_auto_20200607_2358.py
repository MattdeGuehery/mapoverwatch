# Generated by Django 3.0.6 on 2020-06-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapoverwatchapp', '0003_auto_20200603_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_table',
            name='image_map',
            field=models.IntegerField(),
        ),
    ]
