# Generated by Django 4.1.4 on 2023-01-31 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0009_amenity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='amenities',
        ),
    ]