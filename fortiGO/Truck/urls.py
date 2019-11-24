from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='Truck-home'),
    path('register/',views.register,name = 'Truck-register'),
    path('UserPage/', views.UserPage, name='UserPage-home'),
    path('UserPage/Bookings/',views.Bookings, name = 'Bookings-home'),
    path('UserPage/Bookings/UserBookings/',views.UserBookings, name='Routes-home'),
    path('login/',auth_views.LoginView.as_view(template_name = 'Truck/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'Truck/logout.html'),name = 'logout'),

]
