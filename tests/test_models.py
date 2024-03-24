from django.test import TestCase
from restaurant.models import MenuTable, Booking
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import datetime


class MenuTableTestCase(TestCase):
    def setUp(self):
        # Create a MenuTable instance
        MenuTable.objects.create(title='Test Menu Item', price=10.99, inventory=20)

    def test_menu_item_creation(self):
        """Test whether a MenuTable instance is created correctly"""
        menu_item = MenuTable.objects.get(title='Test Menu Item')
        self.assertEqual(menu_item.price, Decimal('10.99'))
        self.assertEqual(menu_item.inventory, 20)


class BookingTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

        # Create a Booking instance
        Booking.objects.create(user=self.user, name='Test Booking', no_of_guests=4, booking_date='2024-04-01')

    def test_booking_creation(self):
        """Test whether a Booking instance is created correctly"""
        booking = Booking.objects.get(name='Test Booking')
        expected_date_string = '2024-04-01'
        self.assertEqual(booking.user.username, 'testuser')
        self.assertEqual(booking.no_of_guests, 4)
        self.assertEqual(booking.booking_date.strftime('%Y-%m-%d'), expected_date_string)
