from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from restaurant.models import Booking


class BookingAuthenticationTest(TestCase):
    # set up the test case by creating two users, a booking object
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='timothy', password='password123')
        self.other_user = User.objects.create_user(username='aline', password='aline123')
        self.booking = Booking.objects.create(user=self.user, name='self.user.name', booking_date='2024-03-25',
                                              no_of_guests='3')

    def test_get_bookings_authenticated(self):
        """
        Test that an authenticated users can retrieve bookings
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/restaurant/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bookings_unauthenticated(self):
        """
        Test that unauthenticated users cannot retrieve any bookings
        """
        response = self.client.get('/api/restaurant/bookings/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_booking_authenticated(self):
        """
        Test that authenticated users can create bookings
        :return:
        """
        self.client.force_authenticate(user=self.user)
        data = {'booking_date': '2024-03-27', 'name': 'timothy', 'no_of_guests': '5'}
        response = self.client.post('/api/restaurant/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_booking_unauthenticated(self):
        """
        Test that unauthenticated users cannot create bookings.
        """
        data = {'booking_date': '2024-03-27', 'name': 'timothy', 'no_of_guests': '5'}
        response = self.client.post('/api/restaurant/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_booking_authenticated(self):
        """
        Test that authenticated users can retrieve only their own bookings.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get(f'/api/restaurant/bookings/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check if all the bookings retrieved belongs to the current user
        bookings = response.data
        for booking in bookings:
            self.assertEqual(booking['username'], self.user.username)

