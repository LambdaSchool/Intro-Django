# Generated by Django 2.1.1 on 2018-09-18 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20180917_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunkBand',
            fields=[
                ('band_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='notes.Band')),
                ('lead_singer', models.TextField(blank=True)),
            ],
            bases=('notes.band',),
        ),
    ]
