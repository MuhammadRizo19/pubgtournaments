from django.shortcuts import render
from .models import Tournament
from django.shortcuts import render
from django.views import generic

def home(request):
    return render(request, 'index.html')

def tourlist(request):
    tournaments = Tournament.objects.all()
    context = {'tournaments' : tournaments}
    return render(request, 'tournament/tourlist.html', context)

class PretourPage(generic.DetailView):
    model = Tournament
    template_name = 'tournament/pretour.html'
    contextual_object_name = 'tour'