# Generated by Django 4.1.4 on 2023-01-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0004_slider_alter_property_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='agent_image')),
                ('full_name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('position', models.CharField(max_length=255)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('twitter', models.URLField(blank=True, max_length=255, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.AddField(
            model_name='property',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]