# Generated by Django 4.1.7 on 2023-04-02 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0052_rename_product_salesregister_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bill', to='POSDemo.storemaster')),
            ],
        ),
        migrations.AddField(
            model_name='salespending',
            name='bill_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='salespending', to='POSDemo.genbill'),
        ),
    ]
