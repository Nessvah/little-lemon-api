from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import MenuTable, Booking


class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuTable
        fields = ['title', 'price', 'inventory']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'url', 'groups']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']