from rest_framework.serializers import ModelSerializer, FloatField, CharField
from django.contrib.auth.models import User
from .models import MenuTable, Booking



class MenuSerializer(ModelSerializer):

    # the price is appearing as string when we send the data
    # but we can override it here
    price = FloatField()

    class Meta:
        model = MenuTable
        fields = ['id', 'title', 'price', 'inventory']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']


class BookingSerializer(ModelSerializer):
    # request.user will return the username and not the actual id
    username = CharField(source='user.username', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'username', 'name', 'no_of_guests', 'booking_date']