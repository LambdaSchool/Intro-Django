# Generated by Django 2.1.2 on 2018-10-24 14:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('img_up', '0003_auto_20181024_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epilepsy',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
