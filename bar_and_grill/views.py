# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import generic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodItem, DrinkItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def food_menu(request):
    return render(request, 'food_menu.html')


def drink_menu(request):
    return render(request, 'drink_menu.html')


class FoodList(generic.ListView):
    """
    This is the view for all food items available on
    the food menu
    """
    model = FoodItem
    queryset = FoodItem.objects.filter(available=1).order_by('-food_type')
    template_name = 'food_menu.html'


class DrinkList(generic.ListView):
    """
    This is the view for all drink items available on
    the drink menu
    """
    model = DrinkItem
    queryset = DrinkItem.objects.filter(available=1).order_by('-drink_type')
    template_name = 'drink_menu.html'
