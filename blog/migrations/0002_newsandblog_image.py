# Generated by Django 4.1.4 on 2023-01-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsandblog',
            name='image',
            field=models.FileField(default='', upload_to='blog_image'),
            preserve_default=False,
        ),
    ]
