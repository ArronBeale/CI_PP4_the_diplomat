# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Table, Guest, Booking
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_name', 'max_seats')


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_id', 'name', 'email', 'phone')
    search_fields = ['name', 'email', 'phone']


@admin.register(Booking)
class BookingAdmim(admin.ModelAdmin):
    list_filter = (
        'guest',
        'guest_count',
        'status',
        'table_id',
        'requested_date',
        'requested_time'
        )
    list_display = ('booking_id', 'guest', 'guest_count', 'status',
                    'table', 'requested_date', 'requested_time')
    search_fields = ['guest__name']
    list_filter = (('requested_date', DateRangeFilter),)
