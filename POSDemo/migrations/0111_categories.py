# Generated by Django 4.1.7 on 2023-04-19 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('POSDemo', '0110_alter_roles_permisssions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.CharField(blank=True, max_length=100)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='category', to='POSDemo.storemaster')),
            ],
        ),
    ]