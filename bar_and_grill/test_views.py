from django.test import TestCase, Client
from django.urls import reverse


class TestMenusViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.food_menu_url = reverse('food_menu')
        self.drink_menu_url = reverse('drink_menu')

    def test_food_menu_GET(self):
        response = self.client.get(self.food_menu_url)

        self.assertEqual(response.status_code, 200)

    def test_drink_menu_GET(self):
        response = self.client.get(self.drink_menu_url)

        self.assertEqual(response.status_code, 200)
