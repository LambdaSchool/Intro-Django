# Generated by Django 2.1.4 on 2018-12-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_money'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money',
            name='choices',
            field=models.CharField(max_length=50, verbose_name=('EARNING_CHOICE', 'bros', 'whateves')),
        ),
    ]
