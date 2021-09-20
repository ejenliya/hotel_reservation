# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from hotel_app.models import Guest, Hotel, Room, Booking

admin.site.register(Guest)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)