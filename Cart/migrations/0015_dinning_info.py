# Generated by Django 4.2 on 2023-07-12 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cart', '0014_rename_shippingaddress_delivery_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinning_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('people', models.IntegerField(blank=True, default=1, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('special_req', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]