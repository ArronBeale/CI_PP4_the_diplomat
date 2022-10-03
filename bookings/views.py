# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Booking
from .forms import BookingForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# This will get the user information if they are logged in

def get_user_instance(request):
    """
    retrieves user details if logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


# Display the booking form and auto fill users email,
# if user is did not provide email it will stay empty


class Reservations(View):
    """
    This view displays the booking form if the user
    is registered and inserts the users email into the
    email field
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
            messages.success(
                request, "Booking succesful, awaiting confirmation")
            return render(request, 'bookings/confirmed.html')

        return render(request, 'bookings/reservations.html',
                      {'booking_form': booking_form})


# Dispays the confirmation page upon a succesful booking


class Confirmed(generic.DetailView):
    """
    This view will display confirmation on a successful booking
    """
    template_name = 'bookings/confirmed.html'

    def get(self, request):
        return render(request, 'bookings/confirmed.html')


# Display all the bookings the user has active,
# bookings older than today will be expired and the
# user will not be able to edit or cancel them once
# expired


class BookingList(generic.ListView):
    """
    This view will display all the bookings
    a particular user has made
    """
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'booking_list.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):

        booking = Booking.objects.all()
        paginator = Paginator(Booking.objects.filter(user=request.user), 4)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)
        today = datetime.datetime.now().date()

        for date in booking:
            if date.requested_date < today:
                date.status = 'Booking Expired'

        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
            return render(
                request,
                'bookings/booking_list.html',
                {
                    'booking': booking,
                    'bookings': bookings,
                    'booking_page': booking_page})
        else:
            return redirect('accounts/login.html')


# Displays the edit booking page and form so the user
# can then change any detail of the booking and update it


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


# Deletes the selected booking the user wishes to cancel

def cancel_booking(request, pk):
    """
    Deletes the booking identified by it's primary key by the user
    """
    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('booking_list')

    return render(
        request, 'bookings/cancel_booking.html', {'booking': booking})
