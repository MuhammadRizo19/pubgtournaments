from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tournaments', views.tourlist, name='tourlist'),
    path('<uuid:pk>/detail', views.PretourPage.as_view(),name='tour_detail'),
]
