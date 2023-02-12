from django.test import TestCase,Client
from restaurant.views import MenuItemsView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.urls import reverse

client=Client()

class MenuItemsViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title='IceCream', Price=80, Inventory=100)
        Menu.objects.create(Title='Jhiar', Price=25, Inventory=120)
        Menu.objects.create(Title='IceCoffe', Price=20, Inventory=96)

    def test_get_all_menuitems(self):
        response=client.get(reverse('menuitems'))
        items=Menu.objects.all()
        serializedItems=MenuSerializer(items,many=True)
        self.assertEqual(response.data,serializedItems.data)
