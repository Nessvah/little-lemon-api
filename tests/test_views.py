from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuTable, Booking, User


class MenuItemViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a test menu item
        MenuTable.objects.create(title='Test Menu Item', price=10.99, inventory=20)

    def test_menu_item_list(self):
        """Test GET request to MenuItemView to list menu items"""
        response = self.client.get('/api/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_menu_item_creation(self):
        """Test POST request to MenuItemView to create a new menu item"""
        data = {'title': 'New Menu Item', 'price': 15.99, 'inventory': 10}
        response = self.client.post('/api/restaurant/menu/', data)
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)  # Should return Unauthorized since permission is restricted
        # to authenticated users


class BookingViewTestCase(TestCase):
    def setUp(self):
        # Create a test booking
        self.user = User.objects.create_user(username='timothy', password='password123')
        Booking.objects.create(user=self.user, name='Test Booking', no_of_guests=4, booking_date='2024-04-01')

    def test_booking_list(self):
        """Test GET request to BookingView to list bookings"""
        response = self.client.get('/api/restaurant/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # because the user isn't login and doesn't
        # provide the necessary credentials

    def test_booking_creation(self):
        """Test POST request to BookingView to create a new booking"""
        data = {'name': 'New Booking', 'no_of_guests': 2, 'booking_date': '2024-05-01'}
        response = self.client.post('/api/restaurant/bookings/', data)
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)  # Should return Unauthorized since permission is restricted
        # to authenticated users
