from django.shortcuts import render
from .models import Tournament,Round,Match
from django.shortcuts import render
from django.views import generic
from datetime import date

def home(request):
    return render(request, 'index.html')

def tourlist(request):
    tournaments = Tournament.objects.all().filter(finished=False)
    context = {'tournaments' : tournaments}
    return render(request, 'tournament/tourlist.html', context)


def tourpage(request,tour_id):
    tour = Tournament.objects.get(id=tour_id)
    if tour.started == True:
        rounds = Round.objects.all().filter(tournament=tour)
        context = {'rounds':rounds}
        return render(request, 'tournament/fixtures.html', context)
    
    else:
        context = {'tournament':tour}
        return render(request, 'tournament/pretour.html', context)

def roundpage(request, round_id):
    rount = Round.objects.get(id=round_id)
    context = {'round':rount}
    return render(request, 'tournament/allgames.html', context)

#for round in rounds:
#matches = Match.objects.all().filter(forround=round)

#class PretourPage(generic.De):
#    model = Tournament
#    template_name = 'tournament/pretour.html'
#    contextual_object_name = 'tour'

#def fixtures(request):
#    return render(request, 'tournament/fixtures.html')