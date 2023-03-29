# Generated by Django 4.1.7 on 2023-03-29 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0037_alter_owner_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessinventorymaster',
            name='action',
            field=models.CharField(choices=[('ADDED', 'product added'), ('REMOVED', 'product removed')], max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='businessinventorymaster',
            name='product_quantity_type',
            field=models.CharField(choices=[('GM', 'gram'), ('PIECE', 'pieces'), ('LTR', 'litre')], max_length=5),
        ),
    ]
