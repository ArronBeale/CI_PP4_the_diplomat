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
    food_list = FoodItem.objects.all()
    return render(
        request, 'bar_and_grill/food_menu.html', {'food_list': food_list})


def drinkMenu(request):
    drink_list = DrinkItem.objects.all()
    return render(
        request, 'bar_and_grill/drink_menu.html', {'drink_list': drink_list})


class FoodList(generic.ListView):
    """
    This is the view for all food items available on
    the food menu
    """
    model = FoodItem
    template_name = 'food_menu.html'
    context = 'food_item'

    def get_queryset(self):
        queryset = {
            'starter_items': FoodItem.objects.all().filter(
                available=True, food_type=0),
            'main_items': FoodItem.objects.all().filter(
                available=True, food_type=1),
            'dessert_items': FoodItem.objects.all().filter(
                available=True, food_type=2)
        }
        return queryset


class DrinkList(generic.ListView):
    """
    This is the view for all food items available on
    the food menu
    """
    model = DrinkItem
    template_name = 'drink_menu.html'
    context = 'drink_item'

    def get_queryset(self):
        queryset = {
            'wine_items': DrinkItem.objects.all().filter(
                available=True, drink_type=0),
            'beer_items': DrinkItem.objects.all().filter(
                available=True, drink_type=1),
            'cocktail_items': DrinkItem.objects.all().filter(
                available=True, drink_type=2)
        }
        return queryset
