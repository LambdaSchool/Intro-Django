# Generated by Django 2.1.4 on 2018-12-04 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelust', '0002_auto_20181204_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('country_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='travelust.Country')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('travelust.country',),
        ),
    ]
