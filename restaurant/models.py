from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.SmallIntegerField()
    booking_date = models.DateTimeField(db_index=True)

    def __str__(self):
        return f"{self.name} - {self.booking_date}"


class MenuTable(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

