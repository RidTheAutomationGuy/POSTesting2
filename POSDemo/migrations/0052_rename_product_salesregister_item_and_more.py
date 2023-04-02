# Generated by Django 4.1.7 on 2023-04-02 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0051_barcode_modeofpayment_transactiondetails_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesregister',
            old_name='product',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='salesregister',
            old_name='product_barcode',
            new_name='item_barcode',
        ),
        migrations.CreateModel(
            name='SalesPending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=100)),
                ('purchase_rate', models.CharField(max_length=20)),
                ('sale_rate', models.CharField(max_length=20)),
                ('row_total', models.CharField(max_length=20)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.business')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.employeemaster')),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.taxmaster')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.storemaster')),
            ],
        ),
    ]
