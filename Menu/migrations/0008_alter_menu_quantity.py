# Generated by Django 4.2 on 2023-07-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0007_alter_menu_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
