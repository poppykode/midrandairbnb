# Generated by Django 4.1.4 on 2023-02-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0019_booking_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
