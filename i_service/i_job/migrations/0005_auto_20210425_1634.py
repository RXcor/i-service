# Generated by Django 3.1.6 on 2021-04-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i_job', '0004_auto_20210418_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='vinner',
            new_name='winner',
        ),
        migrations.AddField(
            model_name='job',
            name='result',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
