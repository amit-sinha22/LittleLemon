from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            Title="IceCream",
            Price=80,
            Inventory=100
        )
        Menu.objects.create(
            Title="Pizza",
            Price=200,
            Inventory=20
        )

    def test_getall(self):
        items = Menu.objects.all()
        serialized_data = MenuItemSerializer(items, many=True).data

        response = self.client.get('/restaurant/menu/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)