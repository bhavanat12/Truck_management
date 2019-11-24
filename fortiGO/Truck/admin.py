from django.contrib import admin
from .models import UserLog, Booking, Routes, Trucks, Truck_status
# Register your models here.
admin.site.register(UserLog)
admin.site.register(Booking)
admin.site.register(Routes)
admin.site.register(Trucks)
admin.site.register(Truck_status)



