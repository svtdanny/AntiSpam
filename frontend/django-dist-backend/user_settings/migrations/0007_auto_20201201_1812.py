# Generated by Django 2.2.13 on 2020-12-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0006_auto_20201201_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillists',
            name='blackList',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maillists',
            name='whiteList',
            field=models.TextField(blank=True, null=True),
        ),
    ]
