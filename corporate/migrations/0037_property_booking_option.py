# Generated by Django 4.1.4 on 2023-02-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0036_rename_deluxe_room_property_deluxe_room_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='booking_option',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
