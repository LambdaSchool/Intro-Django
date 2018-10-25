# Generated by Django 2.1.2 on 2018-10-25 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock_prices', '0004_auto_20181025_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalCompanies',
            fields=[
                ('companies_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock_prices.Companies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('stock_prices.companies',),
        ),
    ]
