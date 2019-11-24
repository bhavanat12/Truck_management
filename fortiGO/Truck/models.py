from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

class DateInput(forms.DateInput):
	input_type = 'date'


class UserLog(models.Model):
    userlogid = models.AutoField(primary_key = True)
    email = models.CharField(max_length = 150)
    password = models.CharField(max_length = 150)
    name = models.CharField(max_length = 150)
    pincode = models.IntegerField()
    date_registered = models.DateTimeField(default = timezone.now)

class Routes(models.Model):
    routeid = models.CharField(primary_key=True, max_length=150)
    start = models.CharField(max_length = 150)
    int_st2 = models.CharField(max_length = 150)
    int_st3 = models.CharField(max_length = 150)
    int_st4 = models.CharField(max_length = 150)
    end = models.CharField(max_length = 150)

class Drivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    driver_name = models.CharField(max_length=150)
    driver_mobile = models.CharField(max_length=150)
    driver_email = models.CharField(max_length=150)


class Trucks(models.Model):
    truck_id = models.CharField(primary_key=True, max_length=150)
    driver_id = models.ForeignKey(Drivers, on_delete=models.PROTECT)
    max_load = models.IntegerField()

class Booking(models.Model):
    user_name = models.CharField(max_length=150)
    user_email = models.CharField(max_length=150)
    booking_id = models.AutoField(primary_key = True)
#    user_id = models.ForeignKey(UserLog,on_delete = models.PROTECT)
#    route_id = models.ForeignKey(Routes,on_delete = models.PROTECT)
#    truck_id = models.ForeignKey(Trucks,on_delete = models.PROTECT)
    source = models.CharField(max_length = 150)
    destination = models.CharField(max_length = 150)
    load_weight = models.IntegerField()
    payment_status = models.CharField(max_length = 150)
    date_booked = models.DateTimeField(default = timezone.now)
    date_journey = models.DateField()


class Truck_status(models.Model):
    truck_id = models.ForeignKey(Trucks, on_delete=models.PROTECT)
    route_id = models.ForeignKey(Routes, on_delete=models.PROTECT)
    starting_date = models.CharField(max_length=150)
    arriving_date = models.CharField(max_length=150)
    truck_weight = models.IntegerField()
