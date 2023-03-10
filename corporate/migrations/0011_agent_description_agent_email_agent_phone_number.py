# Generated by Django 4.1.4 on 2023-01-31 10:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0010_remove_property_amenities'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='description',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='email',
            field=models.EmailField(default='matapelo@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='phone_number',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
