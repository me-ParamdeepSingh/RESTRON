# Generated by Django 4.2 on 2023-06-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_cart_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.CharField(max_length=200),
        ),
    ]
