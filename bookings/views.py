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
from .models import Table, Booking
from .forms import BookingForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def get_user_instance(request, User):
    """ retrieves user details if logged in """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()

    return user


class Reservations(View):
    """
    Renders booking form page
    If user is logged in their email is set as guest email
    """

    template_name = 'bookings/reservations.html'

    def get(self, request, *args, **kwargs):
        booking_form = BookingForm()

        if request.user.is_authenticated:
            user = get_user_instance(request, User)
            if user is None:
                email = request.user.email
                booking_form = BookingForm(initial={'email': email})
            else:
                booking_form = BookingForm()

        else:
            booking_form = BookingForm()

        return render(request, "bookings/reservations.html",
                      {'booking_form': booking_form})

    def post(self, request, User=User, *args, **kwargs):

        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            user_requested_date = request.POST.get('requested_date')
            user_requested_time = request.POST.get('requested_time')
            guest_count = request.POST.get('guest_count')
        else:
            booking_form = BookingForm()

        return render(request, "bookings/reservations.html",
                      {'booking_form': booking_form})
