# Generated by Django 2.1.2 on 2018-10-22 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descrption',
            new_name='description',
        ),
    ]
