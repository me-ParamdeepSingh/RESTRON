# Generated by Django 4.2 on 2023-07-19 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0022_remove_order_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinning_info',
            name='email',
        ),
        migrations.RemoveField(
            model_name='dinning_info',
            name='name',
        ),
    ]