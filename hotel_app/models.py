# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import timedelta, datetime

class Guest(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField(default = 20)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    name = models.CharField(max_length = 20)
    location = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20)
    email = models.CharField(max_length = 30) 

    def __str__(self):
        return self.name

class Room(models.Model):
    room_no = models.IntegerField(default = 101)
    price = models.FloatField(default = 1000.0)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    is_booked = models.BooleanField(default = False)

    def __str__(self):
        return str(self.room_no)

    def hotel_name(self):
        return self.hotel

class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete = models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    num_of_guest = models.IntegerField(default = 1)
    checkin_date = models.DateField(default = datetime.now)
    checkout_date = models.DateField(default = datetime.now)
    is_checkout = models.BooleanField(default = False)

    def __str__(self):
        return self.guest.name

    def hotel_name(self):
        return self.hotel.hotel

    def charge(self):
        return self.is_checkout* \
        (self.checkout_date - self.checkin_date + timedelta(1)).days* \
        self.room.price


