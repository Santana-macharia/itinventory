# Generated by Django 3.1.1 on 2024-01-20 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0015_import_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='import',
            name='assigned_by',
        ),
        migrations.RemoveField(
            model_name='import',
            name='device_name',
        ),
    ]
