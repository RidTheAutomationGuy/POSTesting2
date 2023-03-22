# Generated by Django 4.1.7 on 2023-03-20 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0007_orders_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('adhaar', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='orderes',
        ),
        migrations.AddField(
            model_name='orders',
            name='customer_ordered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='customer_order', to='POSDemo.customer'),
        ),
        migrations.AddField(
            model_name='orders',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_handler', to='POSDemo.employee'),
        ),
    ]
