# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import generic
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodItem, DrinkItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FoodList(generic.ListView):
    """
    This is the view for all food items available on
    the food menu
    """
    model = FoodItem
    queryset = FoodItem.objects.filter(available=1).order_by('-food_name')
    template_name = 'menu.html'


class DrinkList(generic.ListView):
    """
    This is the view for all drink items available on
    the drink menu
    """
    model = DrinkItem
    queryset = DrinkItem.objects.filter(available=1).order_by('-drink_name')
    template_name = 'menu.html'
