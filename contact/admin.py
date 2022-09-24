# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from rangefilter.filters import DateRangeFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Contact
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'created_date'
        )
    list_display = (
        'message_id',
        'user',
        'name',
        'message',
        'phone',
        'created_date')

    search_fields = ['name']
    list_filter = (('created_date', DateRangeFilter),)
