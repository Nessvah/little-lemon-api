from rest_framework.serializers import ModelSerializer, FloatField, PrimaryKeyRelatedField
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
        fields = ['username', 'email', 'url', 'groups']


class BookingSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Booking
        fields = ['id', 'user', 'name', 'no_of_guests', 'booking_date']