# Generated by Django 2.2.13 on 2020-12-01 21:17

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_settings', '0007_auto_20201201_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maillists',
            name='id',
        ),
        migrations.AddField(
            model_name='maillists',
            name='_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='maillists',
            name='blackList',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='maillists',
            name='whiteList',
            field=models.TextField(null=True),
        ),
    ]
