from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tournaments', views.tourlist, name='tourlist'),
    path('alltournaments', views.advancedtourlist, name='advancedtourlist'),
    #path('fixtures', views.fixtures, name='fixtures'),
    path('<uuid:tour_id>/detail', views.tourpage,name='tour_detail'),
    path('<uuid:pk>/edit/',views.EditTour.as_view(), name='edittour'),
    #path('<uuid:round_id>/detail', views.roundpage,name='round_detail'),
]
