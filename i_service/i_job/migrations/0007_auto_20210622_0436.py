# Generated by Django 3.1.6 on 2021-06-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i_job', '0006_auto_20210425_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
