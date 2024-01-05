# Generated by Django 4.2 on 2023-07-03 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0004_remove_menu_in_cart_remove_menu_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='in_cart',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menu',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
