# Generated by Django 4.1.7 on 2023-04-12 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0097_remove_employeemaster_store_employeemaster_business'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeauth',
            name='store',
        ),
        migrations.AddField(
            model_name='employeeauth',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee_auth', to='POSDemo.business'),
        ),
    ]