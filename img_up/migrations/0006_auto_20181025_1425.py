# Generated by Django 2.1.2 on 2018-10-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_up', '0005_epilepsyuserinput_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epilepsy',
            name='numOfAdultCases',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='epilepsy',
            name='numOfChildCases',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='epilepsy',
            name='numOfTotalCases',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
