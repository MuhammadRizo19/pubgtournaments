from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tournaments', views.tourlist, name='tourlist'),
    #path('fixtures', views.fixtures, name='fixtures'),
    path('<uuid:tour_id>/detail', views.tourpage,name='tour_detail'),
    path('<uuid:round_id>/detail', views.roundpage,name='round_detail'),
]
