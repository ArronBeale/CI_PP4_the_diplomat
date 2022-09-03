# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
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
    The user email is set as booking email
    """

    template_name = 'bookings/reservations.html'

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input
        """

        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'bookings/reservations.html',
                      {'booking_form': booking_form})

    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database
        """

        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect(Confirmed())
        else:
            booking_form = BookingForm()

        return render(request, 'bookings/confirmed.html')


class Confirmed(generic.DetailView):
    """
    Renders the confirmation page
    """
    template_name = 'bookings/confirmed.html'

    def get(self, request):
        return render(request, 'bookings/confirmed.html')
