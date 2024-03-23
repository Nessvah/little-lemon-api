from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .models import MenuTable, Booking, User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin


def index(request):
    return render(request, 'index.html', {})


def home(request):
    return HttpResponse('hello world')


# ListCreateAPIView is a generic view from drf that provides listing and
# creation functionality for a resource
class MenuItemView(ListCreateAPIView):
    # this will retrieve all objects from the database
    queryset = MenuTable.objects.all()

    # this specifies how the data from the model should be serialized or
    # deserialized for the API
    serializer_class = MenuSerializer

    # this method will return a list of permissions classes to apply to this view
    def get_permissions(self):
        permission_classes = []
        if self.request.method == 'POST':
            print('damn')
            # if the request it's a post only a user can access
            permission_classes = [IsAdminUser]
        # It iterates over each class in permission_classes, instantiates it,
        # and adds the instance to the list.
        return [permission() for permission in permission_classes]


class MenuItemDetail(RetrieveUpdateDestroyAPIView):
    queryset = MenuTable.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        print(self.request.user)
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class BookingView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # only authenticated users can access these views
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    # # Users can only view their own bookings unless they are admin
    def get_queryset(self):
        # get the user that is making the request
        user = self.request.user
        print(user.is_staff)
        # check if the user is a staff and if it is,
        # can see all bookings
        if user.is_staff:
            return Booking.objects.all()
        else:
            return Booking.objects.filter(user=user)

    # while creating we need to associate the booking with the
    # user who makes the request
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    permission_classes = [IsAuthenticated]
