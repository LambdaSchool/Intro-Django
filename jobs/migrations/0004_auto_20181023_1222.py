# Generated by Django 2.1.2 on 2018-10-23 19:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_remove_job_date_found'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
