# Generated by Django 3.2.15 on 2022-08-18 19:41

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('table_id', models.AutoField(primary_key=True, serialize=False)),
                ('table_name', models.CharField(default='New Table', max_length=50, unique=True)),
                ('max_seats', models.IntegerField()),
            ],
            options={
                'ordering': ['-max_seats'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('requested_date', models.DateField()),
                ('requested_time', models.CharField(choices=[('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00')], default='17:00', max_length=25)),
                ('status', models.CharField(choices=[('awaiting confirmation', 'awaiting confirmation'), ('booking confirmed', 'booking confirmed'), ('booking rejected', 'booking rejected'), ('booking expired', 'booking expired')], default='awaiting confirmation', max_length=25, unique=True)),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table_reserved', to='bookings.table')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='bookings.user')),
            ],
            options={
                'ordering': ['-requested_time'],
            },
        ),
    ]
