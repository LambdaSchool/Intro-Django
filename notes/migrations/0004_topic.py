# Generated by Django 2.1.1 on 2018-09-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_personalnote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_name', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
