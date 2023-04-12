# Generated by Django 4.1.7 on 2023-04-12 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0091_rename_dealermaster_suppliermaster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchaseregister',
            old_name='dealer',
            new_name='supplier',
        ),
        migrations.AddField(
            model_name='purchaseregister',
            name='store',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='purchaseregister', to='POSDemo.storemaster'),
        ),
    ]
