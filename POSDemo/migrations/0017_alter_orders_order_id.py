# Generated by Django 4.1.7 on 2023-03-22 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0016_alter_orders_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_id',
            field=models.IntegerField(),
        ),
    ]
