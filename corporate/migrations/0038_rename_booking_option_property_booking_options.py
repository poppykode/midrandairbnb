# Generated by Django 4.1.4 on 2023-02-27 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0037_property_booking_option'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='booking_option',
            new_name='booking_options',
        ),
    ]
