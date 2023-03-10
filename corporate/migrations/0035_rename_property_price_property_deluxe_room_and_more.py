# Generated by Django 4.1.4 on 2023-02-27 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0034_alter_generalpage_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='property_price',
            new_name='deluxe_room',
        ),
        migrations.AddField(
            model_name='property',
            name='deluxe_room_with_patio',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='property',
            name='full_property_price',
            field=models.FloatField(default=0.0),
        ),
    ]
