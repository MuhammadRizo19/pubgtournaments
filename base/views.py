from django.shortcuts import render
from .models import Tournament, Round, Match
from django.shortcuts import render
from django.views import generic
from datetime import date

def home(request):
    return render(request, 'index.html')

def tourlist(request):
    tournaments = Tournament.objects.all().filter(finished=False)
    context = {'tournaments' : tournaments}
    return render(request, 'tournament/tourlist.html', context)

class PretourPage(generic.DetailView):
    model = Tournament
    template_name = 'tournament/pretour.html'
    contextual_object_name = 'tour'

def fixtures(request):
#    tournament = Tournament.objects.get(finished=False)
#    matches = Match.objects.all().filter(tournament=tournament)
    matches = Match.objects.all()
    context = {
        'matches': matches
    }
    return render(request, 'tournament/fixtures.html', context)