# Generated by Django 4.1.4 on 2023-02-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0021_bookingidtracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingidtracker',
            name='booking_id',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
