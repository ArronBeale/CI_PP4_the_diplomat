# Generated by Django 3.2.15 on 2022-09-22 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_booking_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('requested_date', 'requested_time', 'table')},
        ),
    ]