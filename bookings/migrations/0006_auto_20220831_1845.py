# Generated by Django 3.2.15 on 2022-08-31 18:45

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20220831_1822'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
