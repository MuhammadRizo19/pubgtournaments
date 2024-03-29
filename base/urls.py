from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tournaments', views.tourlist, name='tourlist'),
    path('alltournaments', views.advancedtourlist, name='advancedtourlist'),
    path('<uuid:tour_id>/detail', views.tourpage,name='tour_detail'),
    path('<uuid:rnd_id>/delete', views.deleteround, name='deleteround'),
    path('<uuid:rnd_id>/view', views.roundview, name='roundview'),
    path('<uuid:tour_id>/alldetail', views.tourdetail,name='tour_detailall'),
    path('<uuid:pk>/edit/',views.EditTour.as_view(), name='edittour'),
    path('<uuid:pk>/approval/',views.ApprovalRequest.as_view(), name='approval'),
    path('<uuid:tour_id>/createround', views.createround, name='createround'),
    path('advanced', views.advanced, name='advanced'),
    #path('<uuid:round_id>/detail', views.roundpage,name='round_detail'),
    #path('fixtures', views.fixtures, name='fixtures'),
]
