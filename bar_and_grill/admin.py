# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodItem, DrinkItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):
    list_display = ('food_name', 'food_type', 'price', 'available')
    search_fields = ('food_name', 'description')
    list_filter = ('available', 'food_type')
    summernote_fields = ('description')


@admin.register(DrinkItem)
class DrinkAdmin(SummernoteModelAdmin):
    list_display = ('drink_name', 'drink_type', 'price', 'available')
    search_fields = ('drink_name', 'description')
    list_filter = ('available', 'drink_type')
    summernote_fields = ('description')
