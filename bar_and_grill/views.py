# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import generic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodItem, DrinkItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def foodMenu(request):
    """
    a view to display the food menu
    """
    food_list = FoodItem.objects.all()
    return render(
        request, 'bar_and_grill/food_menu.html', {'food_list': food_list})


def drinkMenu(request):
    """
    a view to display the drinks menu
    """
    drink_list = DrinkItem.objects.all()
    return render(
        request, 'bar_and_grill/drink_menu.html', {'drink_list': drink_list})
