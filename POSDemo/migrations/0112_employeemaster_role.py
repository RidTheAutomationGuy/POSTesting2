# Generated by Django 4.1.7 on 2023-04-19 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0111_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeemaster',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='employee', to='POSDemo.roles'),
        ),
    ]