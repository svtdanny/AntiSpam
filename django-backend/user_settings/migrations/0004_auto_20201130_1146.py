# Generated by Django 2.2.13 on 2020-11-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0003_auto_20201130_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classsettings',
            name='ClassSets',
            field=models.IntegerField(),
        ),
    ]
