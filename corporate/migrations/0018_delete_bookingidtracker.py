# Generated by Django 4.1.4 on 2023-02-06 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0017_alter_bookingidtracker_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingIdTracker',
        ),
    ]