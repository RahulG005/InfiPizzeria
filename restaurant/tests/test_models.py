# tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import Menuserializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory = 12)
        self.menu2 = Menu.objects.create(title="Burger", price=8.99, inventory = 35)
        self.menu3 = Menu.objects.create(title="Pasta", price=12.99, inventory = 20)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = Menuserializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

# To run the test, use the command:
# python manage.py test


