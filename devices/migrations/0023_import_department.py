# Generated by Django 3.2.23 on 2024-01-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0022_remove_import_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='import',
            name='department',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
