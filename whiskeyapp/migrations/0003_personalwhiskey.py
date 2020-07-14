# Generated by Django 2.1.2 on 2018-10-23 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whiskeyapp', '0002_auto_20181023_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalWhiskey',
            fields=[
                ('whiskey_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='whiskeyapp.Whiskey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('whiskeyapp.whiskey',),
        ),
    ]
