# Generated by Django 2.1.2 on 2018-10-24 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('genres', '0003_auto_20181024_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalMusic',
            fields=[
                ('genre_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='genres.Genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('genres.genre',),
        ),
    ]
