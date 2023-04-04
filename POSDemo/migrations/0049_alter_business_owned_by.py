# Generated by Django 4.1.7 on 2023-04-01 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0048_taxmaster_product_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='owned_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='business', to='POSDemo.owner'),
        ),
    ]