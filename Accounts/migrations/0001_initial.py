# Generated by Django 4.2 on 2023-07-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_no', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=100)),
            ],
        ),
    ]
