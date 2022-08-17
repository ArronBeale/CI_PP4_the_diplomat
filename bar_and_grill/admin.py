from django.contrib import admin
from .models import FoodItem, DrinkItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FoodItem)
class FoodAdmin(SummernoteModelAdmin):
    list_filter = ('available', 'food_type')
    summernote_fields = ('description')


@admin.register(DrinkItem)
class DrinkAdmin(SummernoteModelAdmin):
    list_filter = ('available', 'drink_type')
    summernote_fields = ('description')
