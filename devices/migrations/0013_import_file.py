# Generated by Django 3.1.1 on 2024-01-19 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0012_auto_20240119_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='import',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
    ]