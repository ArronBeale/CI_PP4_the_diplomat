# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal:
from bookings import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('reservations/', views.Reservations.as_view(), name='reservations'),
    path('confirmed/', views.Confirmed.as_view(), name='confirmed'),
    path('booking_list/', views.BookingList.as_view(), name='booking_list'),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit_booking'),
]
