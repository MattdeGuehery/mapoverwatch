# Generated by Django 3.0.6 on 2020-06-08 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapoverwatchapp', '0004_auto_20200607_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_table',
            name='image_url',
            field=models.CharField(max_length=300),
        ),
    ]
