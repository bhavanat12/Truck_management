from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking,Routes

class DateInput(forms.DateInput):
	input_type = 'date'



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    pincode = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username','email','password1','password2','pincode']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class BookingForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ['user_name', 'user_email', 'source', 'destination', 'load_weight', 'date_journey']
		widgets = {'date_journey':DateInput()}
				
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


	def clean_email(self):
		email = self.cleaned_data.get('user_email')
		source = self.cleaned_data.get('source')
		destination = self.cleaned_data.get('destination')
		if validate_route(source,destination) == 1:
			raise forms.ValidationError(u'You are fucked up')
		return email

