# Generated by Django 5.0.1 on 2024-11-11 15:04

import ad.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, upload_to=ad.models.file_location),
        ),
    ]