# Generated by Django 4.1.4 on 2023-01-31 07:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0007_property_no_of_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='whats_near_by',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
