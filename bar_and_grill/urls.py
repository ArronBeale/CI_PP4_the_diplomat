# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# Internal:
from bar_and_grill import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Urls for the food and drinks menu
urlpatterns = [
    path('food_menu', views.food_menu, name='food_menu'),
    path('drink_menu', views.drink_menu, name='drink_menu'),
]
