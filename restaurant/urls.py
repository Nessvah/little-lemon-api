
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.MenuItemDetail.as_view()),
    path('bookings/', views.BookingView.as_view()),
    path('bookings/<int:pk>', views.BookingDetail.as_view()),
]
