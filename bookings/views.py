# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.views import generic
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Table, Booking
from .forms import BookingForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def get_user_instance(request):
    """ retrieves user details if logged in """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class Reservations(View):
    """
    Renders booking form page for registered user
    The user email is set as booking email
    """
    template_name = 'bookings/reservations.html'
    success_message = 'Booking has been made.'

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
            return render(request, 'bookings/confirmed.html')
        else:
            messages.warning(
                request, 'Please use correct format')
            booking_form = BookingForm()
        return render(request, 'bookings/reservations.html',
                      {'booking_form': booking_form})


class Confirmed(generic.DetailView):
    """
    Renders the confirmation page
    """
    template_name = 'bookings/confirmed.html'

    def get(self, request):
        return render(request, 'bookings/reservations.html')


class BookingList(generic.DetailView):
    """
    This view will display all the bookings
    a particular user has made
    """
    template_name = 'booking_list.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
            return render(
                request, 'bookings/booking_list.html', {'bookings': bookings})
        else:
            return redirect('accounts/login.html')


class EditBooking(SuccessMessageMixin, UpdateView):
    """
    This view will display the booking by it's primary key
    so the user can then edit it
    """
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_message = 'Booking has been updated.'

    def get_success_url(self, **kwargs):
        return reverse('booking_list')
