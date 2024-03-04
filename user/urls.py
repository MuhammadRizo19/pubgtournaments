from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('logout', views.logoutuser, name='logout'),
    path('login', views.loginuser, name='login'),
    path('<uuid:pro_id>/view/',views.profiledetail, name='profile'),
    #path('<uuid:pro_id>/edit/',views.editprofile, name='editprofile'),
    path('<uuid:pk>/update',views.UpdateProfile.as_view(),name='editprofile'),
    path('users', views.allusers, name='allusers'),
    path('<uuid:pr_id>/view/',views.profileview, name='profileview'),
    path('leadersboard', views.leadersboard, name='leadersboard'),
]
