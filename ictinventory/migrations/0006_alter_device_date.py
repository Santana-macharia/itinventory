# Generated by Django 5.0.1 on 2024-01-05 08:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ictinventory', '0005_alter_device_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
