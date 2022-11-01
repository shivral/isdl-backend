from django.urls import path,re_path
from .views import api_home, logout,register,login, userView,getAllHalls
from .user_views import createBooking,getUserBooking
from .hall_views import createHall
from .admin_views import acceptRequest, registerAdmin,loginAdmin,getAllPending
urlpatterns = [
    path('home',api_home),
    path('register',register),
    path('login',login),
    path('user',userView),
    path('logout',logout),
    path('createBooking',createBooking),
    path('createHall',createHall),
    path('allHalls',getAllHalls),
    path('getUserBookings',getUserBooking),
    path('registerAdmin',registerAdmin),
    path('loginAdmin',loginAdmin),
    path('getAllPending',getAllPending),
    path('acceptRequest',acceptRequest)
]
