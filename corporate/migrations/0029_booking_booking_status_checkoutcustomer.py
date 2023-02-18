# Generated by Django 4.1.4 on 2023-02-06 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corporate', '0028_alter_property_property_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_status',
            field=models.CharField(choices=[('active', 'Active'), ('checked in', 'Checked In'), ('cancelled', 'Cancelled'), ('checked out', 'checked out')], default='active', max_length=100),
        ),
        migrations.CreateModel(
            name='CheckOutCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_property', to='corporate.property')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
