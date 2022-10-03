# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Model for the contact item in the database


class Contact(models.Model):
    """
    a class for the Contact model
    """
    message_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contact_user",
        null=True
        )
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    phone = PhoneNumberField(null=True)
    message = models.TextField()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name
