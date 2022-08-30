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


class Reservations(View):
    """ Reservation view for guests to make bookings """

    def get(self, request, *args, **kwargs):

        template_name = "bookings/reservations.html"

        return render(request, "bookings/reservations.html",
                      {'guest_form': GuestForm(),
                       'booking_form': BookingForm()})

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
