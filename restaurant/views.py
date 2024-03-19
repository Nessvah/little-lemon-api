from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .models import MenuTable, Booking, User

def index(request):
    return render(request, 'index.html', {})


def home(request):
    return HttpResponse('hello world')


class MenuItemView(ListCreateAPIView):

    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer


class MenuItemDetail(RetrieveUpdateDestroyAPIView):

    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer