# Generated by Django 4.2 on 2023-07-02 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_menu_quantity'),
        ('Cart', '0002_alter_cart_items_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_items',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='Menu.menu'),
        ),
    ]