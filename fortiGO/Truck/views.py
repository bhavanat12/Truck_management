from django.shortcuts import render,redirect
from .models import UserLog, Booking
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import BookingForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Routes



'''class DateInput(forms.DateInput):
	input_type = 'date'

start_date = DateInput()'''


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created Successfully for {username}!')
            return redirect('UserPage-home')
    else:
        form = UserRegistrationForm()
    return render(request,'Truck/index.html',{'form':form})

@login_required
def UserBookings(request):
    if request.method == 'POST':
        print("bkjcscvjns")
        form_1 = BookingForm(request.POST)
        if form_1.is_valid():
            errors = []
            source = form_1.cleaned_data.get('source')
            destination = form_1.cleaned_data.get('destination')
            '''if validate_route(source,destination) == 0:
                form_1.save()
                return redirect('UserPage-home')
            else:
                errors.append('You are out')'''
    else:
        form_1 = BookingForm()
    return render(request,'Truck/bookings_1.html',{'form_1':form_1})

def validate_route(source,destination):
    temp_source = source
    temp_destination = destination
    route_ids = ['MUMHYD','MUMCHE','MUMBAN','HYDMUM','HYDBAN','HYDCHE','CHEMUM','CHEHYD','CHEBAN','BANMUM','BANHYD','BANCHE']
    route = Routes.objects.all()
    start =[]
    int_1 = []
    int_2 = []
    int_3 = []
    end = []

    route_list = Routes.objects.all()
    for route in route_list:
        start.append(route.start)
        int_1.append(route.int_st2)
        int_2.append(route.int_st3)
        int_3.append(route.int_st4)
        end.append(route.end)

    for i in range(12):
        temp_source = -1
        temp_destination = -1

        routes = [start[i],int_1[i],int_2[i],int_3[i],end[i]]
        for j in range(5):
            if source == routes[j]:
                temp_source = j
            if destination == routes[j]:
                temp_destination = j

        if temp_source < temp_destination and temp_source != -1 and temp_destination != -1 :
            return 0

    return 1









#from Truck import signup
# Create your views here.

def home(request):
	return render(request, 'Truck/MainPage.html')
def signup(request):
	return render(request,'Truck/signup.html')

'''def register(request):
	print(request.POST)
	email = request.POST['email']
	password = request.POST['password']
	name = request.POST['name']
	pincode = request.POST['pincode']
	if UserLog.objects.filter(email = email):
		#messages.info(request,f'User Already Exists')
		return render(request,'Truck/signup.html',)
	userlog = UserLog.objects.create(email = email,password = password,name = name,pincode = pincode)
	print("You are Registered Successfully")
	return render(request,'Truck/base.html')'''

@login_required
def Payment_valid(request):
	if request.method == 'POST':
		form_2 = PaymentForm(request.POST)
		if form_2.is_valid():
			messages.success(request, f'Payment successful!')
			form_2.save()
			return render(request, 'Truck/UserPage.html')
	else:
		form_2 = PaymentForm()
	return render(request,'Truck/payments.html',{'form_2':form_2})


def Payments(request,):
	return render(request, 'Truck/payments.html')



def UserPage(request):
	return render(request, 'Truck/UserPage.html')

def Bookings(request):
	return render(request, 'Truck/bookings_1.html')

'''def UserBookings(request):
	print("Request Object :{}".format(request.POST))
	fullname = request.POST['field1']
	email = request.POST['field2']
	source = request.POST['field4']
	destination = request.POST['field5']
	load = request.POST['field6']
	booking = Booking.objects.create(user_name=fullname,user_email=email,source=source,destination=destination,load_weight=load)
	return render(request, 'Truck/MainPage.html')'''
