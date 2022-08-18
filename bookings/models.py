from django.db import models


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
