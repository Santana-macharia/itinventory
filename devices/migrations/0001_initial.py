# Generated by Django 3.1.1 on 2024-01-08 19:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ictinventory', '0007_auto_20240107_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alldevices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware', models.CharField(max_length=200)),
                ('system_model', models.CharField(max_length=200)),
                ('processor', models.CharField(max_length=200)),
                ('ram', models.CharField(max_length=100)),
                ('hdd', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Issued', 'Issued'), ('Not Issued', 'Not Issued'), ('Returned', 'Returned')], max_length=100)),
                ('physicalconfirmation', models.CharField(choices=[('Correct', 'Correct'), ('Incorrect', 'Incorrect')], max_length=100)),
                ('uaf_signed', models.CharField(choices=[('Yes', 'No'), ('Yes', 'No')], max_length=100)),
                ('comments', models.CharField(max_length=500)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.mohiuser')),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ictinventory.centre')),
            ],
        ),
    ]