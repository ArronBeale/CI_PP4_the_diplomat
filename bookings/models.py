# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Restaurant first sitting at noon and last sitting 11pm
time_slots = (
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
    ('23:00', '23:00'),
)


# Status options inspired by the JustEat status' when ordering
status_options = (
    ('awaiting confirmation', 'awaiting confirmation'),
    ('booking confirmed', 'booking confirmed'),
    ('booking rejected', 'booking rejected'),
    ('booking expired', 'booking expired'),
)


class Table(models.Model):
    """
    a class for the Table model
    """
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(
        max_length=50, default='New Table', unique=True)
    max_seats = models.IntegerField()

    class Meta:
        ordering = ['-max_seats']

    def __str__(self):
        return self.table_name


class User(models.Model):
    """
    a class for the User model
    """
    user_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=254, default="")
    phone = PhoneNumberField()

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.user_id


class Booking(models.Model):
    """
    a class for the Booking model
    """
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=25, choices=time_slots, default='17:00')
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name="table_reserved",
        null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    status = models.CharField(
        max_length=25, choices=status_options,
        default='awaiting confirmation', unique=True)
    seats = (
        (1, "1 guest"),
        (2, "2 guests"),
        (3, "3 guests"),
        (4, "4 guests"),
        (5, "5 guests"),
        (6, "6 guests"),
        )

    class Meta:
        ordering = ['-requested_time']

    def __str__(self):
        return self.booking_id
