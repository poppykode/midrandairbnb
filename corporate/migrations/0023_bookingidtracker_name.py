# Generated by Django 4.1.4 on 2023-02-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0022_alter_bookingidtracker_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingidtracker',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
