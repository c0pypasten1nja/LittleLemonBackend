from django.test import TestCase
from restaurant.models import Menu  # Replace 'yourapp' with your actual app name
from restaurant.views import MenuItemsView  # Import your view


class MenuModelTest(TestCase):
    def test_menu_item_str(self):
        item = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

