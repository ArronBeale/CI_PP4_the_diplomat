# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Table, Guest, Booking
from .forms import BookingForm, GuestForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def get_guest_instance(request, User):
    """ retrieves user details if logged in """

    guest_email = request.user.email
    guest = Guest.objects.filter(email=guest_email).first()

    return guest


class Reservations(View):
    """ Reservation view for guests to make bookings """

    template_name = 'bookings/reservations.html'

    def get(self, request, *args, **kwargs):
        booking_form = BookingForm()

        if request.user.is_authenticated:
            guest = get_guest_instance(request, User)
            if guest is None:
                email = request.user.email
                guest_form = GuestForm(initial={'email': email})
            else:
                guest_form = GuestForm(instance=guest)
                booking_form = BookingForm()

        else:
            guest_form = GuestForm()
            booking_form = BookingForm()

        return render(request, "bookings/reservations.html",
                      {'guest_form': guest_form,
                       'booking_form': booking_form})

    def post(self, request, User=User, *args, **kwargs):

        guest_form = GuestForm(data=request.POST)
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid() and guest_form.is_valid():
            guest_requested_date = request.POST.get('requested_date')
            guest_requested_time = request.POST.get('requested_time')
            guest_count = request.POST.get('guest_count')
        else:
            booking_form = BookingForm()

        return render(request, "bookings/reservations.html",
                      {'guest_form': guest_form,
                       'booking_form': booking_form})
