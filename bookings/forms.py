from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    requested_date = forms.DateField()

    class Meta:
        model = Booking
        fields = ('guest_count', 'requested_date', 'requested_time')
