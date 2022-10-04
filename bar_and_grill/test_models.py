# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.test import TestCase
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import FoodItem, DrinkItem
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestModels(TestCase):

    def test_new_foods(self):
        food = FoodItem.objects.create(
            food_name='Test Food',
            description='Test description',
            price='9.99',
            food_type=1
            )
        self.assertFalse(food.available)
        self.assertEqual(food.price, '9.99')
        self.assertEqual(food.description, 'Test description')

    def test_new_drinks(self):
        drink = DrinkItem.objects.create(
            drink_name='Test drink',
            description='Test description',
            price='9.99',
            drink_type=1
            )
        self.assertFalse(drink.available)
        self.assertEqual(drink.price, '9.99')
        self.assertEqual(drink.description, 'Test description')
