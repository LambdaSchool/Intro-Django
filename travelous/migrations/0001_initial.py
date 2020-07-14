# Generated by Django 2.1.4 on 2018-12-04 15:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=200)),
                ('capital', models.TextField(blank=True)),
                ('wiki', models.URLField()),
                ('visited', models.BooleanField(default=False)),
            ],
        ),
    ]
