from .models import Tournament,Round,Match
from django.shortcuts import render,redirect
from django.views import generic
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from .forms import EditTournamentForm 
from django.urls import reverse_lazy

def home(request):
    return render(request, 'index.html')

class EditTour(LoginRequiredMixin,generic.UpdateView):
    model = Tournament
    form_class = EditTournamentForm
    success_url = reverse_lazy('advancedtourlist')
    template_name = 'forstaff/edittour.html'

   # def dispatch(self, request, *args, **kwargs): # new
   #      obj = self.get_object()
   #      if obj.author != self.request.user:
   #           raise PermissionDenied
   #      return super().dispatch(request, *args, **kwargs)

def tourlist(request):
    tournaments = Tournament.objects.all().filter(finished=False)
    context = {'tournaments' : tournaments}
    return render(request, 'tournament/tourlist.html', context)

def advancedtourlist(request):
    tournaments = Tournament.objects.all()
    context = {'tournaments' : tournaments}
    return render(request, 'forstaff/tourlist.html', context)


def tourpage(request,tour_id):
    tour = Tournament.objects.get(id=tour_id)
    if tour.started == True:
        rounds = Round.objects.all().filter(tournament=tour)
        for round in rounds:
            matches = Match.objects.all().filter(forround=round)
        context = {'rounds':rounds, 'matches':matches}
        return render(request, 'tournament/fixtures.html', context)
    
    else:
        context = {'tournament':tour}
        return render(request, 'tournament/pretour.html', context)

"""""
def roundpage(request, round_id):
    rount = Round.objects.get(id=round_id)
    context = {'round':rount}
    return render(request, 'tournament/allgames.html', context)
"""""

#class PretourPage(generic.De):
#    model = Tournament
#    template_name = 'tournament/pretour.html'
#    contextual_object_name = 'tour'

#def fixtures(request):
#    return render(request, 'tournament/fixtures.html')