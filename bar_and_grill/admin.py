from django.contrib import admin
from .models import FoodItem, DrinkItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(FoodItem())
class FoodAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


@admin.register(DrinkItem())
class DrinkAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
