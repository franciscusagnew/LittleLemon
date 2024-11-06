from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from rest_framework import status
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu

# Create your tests here.
class MenuItemsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="admin", email="admin@littlelemon.com", password="admin")

    def test_view(self):
        request = self.factory.get('/api/menu/')
        request.user = self.user
        response = MenuItemsView.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)