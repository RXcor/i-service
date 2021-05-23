# Generated by Django 3.1.6 on 2021-04-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('i_job', '0002_auto_20210222_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='progress',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='vinner',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='type_of',
            field=models.IntegerField(choices=[(0, 'Лайки по лайктайму'), (1, 'Лайки по хэштегам'), (2, 'Подписки по хэштегам'), (3, 'Отписка от неподписаных'), (4, 'Отписка от всех'), (5, 'Игра'), (6, 'Розыгрыш')]),
        ),
    ]
