from django.db import models

time_slots = (

)




class Table(models.Model):
    """
    a class for the table model
    """
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(
        max_length=50, default='New Table', unique=True)
    max_seats = models.IntegerField()

    class Meta:
        ordering = ['-max_seats']

    def __str__(self):
        return self.table_name


class Booking(models.Model):
    """
    a class for the booking model
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
    status = models.CharField(max_length=25, unique=True)

    class Meta:
        ordering = ['-requested_time']

    def __str__(self):
        return self.booking_id


class User(models.Model):
