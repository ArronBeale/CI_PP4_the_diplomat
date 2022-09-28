# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import SimpleTestCase
from django.urls import reverse, resolve
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from bar_and_grill.views import food_menu, drink_menu
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestMenuUrls(SimpleTestCase):
    """
    This class is for testing the food
    and drink menu urls
    """
    def test_food_menu_resolved(self):
        url = reverse('food_menu')
        self.assertEquals(resolve(url).func, food_menu)

    def test_drink_menu_resolved(self):
        url = reverse('drink_menu')
        self.assertEquals(resolve(url).func, drink_menu)
