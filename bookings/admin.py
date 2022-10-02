# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from rangefilter.filters import DateRangeFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Table, Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Registration of tables to display in the admin panel
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_name', 'max_seats')


# Registration of bookings to display in the admin panel
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'guest_count',
        'status',
        'table_id',
        'requested_date',
        'requested_time',
        'created_date'
        )
    list_display = (
        'booking_id',
        'user',
        'name',
        'phone',
        'guest_count',
        'status',
        'table',
        'requested_date',
        'requested_time',
        'created_date')

    search_fields = ['guest__name']
    list_filter = (('requested_date', DateRangeFilter),)
    actions = ['confirm_bookings']

    def confirm_bookings(self, request, queryset):
        queryset.update(status='Booking Confirmed')
