# Generated by Django 3.1.6 on 2021-02-14 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=255)),
                ('password', models.CharField(blank=True, max_length=512, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=30, null=True)),
                ('like_limit_for_job', models.IntegerField(blank=True, null=True)),
                ('follow_limit_for_job', models.IntegerField(blank=True, null=True)),
                ('unfollow_limit_for_job', models.IntegerField(blank=True, null=True)),
                ('comment_limit_for_job', models.IntegerField(blank=True, null=True)),
                ('is_busines', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
