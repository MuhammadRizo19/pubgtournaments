from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('logout', views.logoutuser, name='logout'),
    path('login', views.loginuser, name='login'),
     path('<uuid:pro_id>/view/',views.profiledetail, name='profile'),
]
