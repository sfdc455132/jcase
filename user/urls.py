from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
<<<<<<< HEAD
    path('register/',views.user_register,name='register'),
    path('profile/<str:id>',views.profile,name='profile'),
=======
>>>>>>> abdea342ff039d1da254873cd0223bd9700dfe7a
]
