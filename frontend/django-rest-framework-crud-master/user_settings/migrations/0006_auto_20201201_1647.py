# Generated by Django 2.2.13 on 2020-12-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0005_auto_20201201_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillists',
            name='blackList',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='maillists',
            name='whiteList',
            field=models.TextField(),
        ),
    ]
