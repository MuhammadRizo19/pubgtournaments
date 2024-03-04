from .models import Tournament,Round,Match, Request, Participant
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.views import generic
from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from .forms import EditTournamentForm,RequestForm,ApprovalRequestForm, RoundCreationForm
from django.urls import reverse_lazy
from user.models import Profile 

@login_required(login_url="account/login")
def home(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}
    return render(request, 'index.html', context)


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
    waiting = Request.objects.all().filter(checked=False).count()
    context = {'tournaments' : tournaments, 'waiting':waiting}
    return render(request, 'forstaff/tourlist.html', context)

def tourpage(request,tour_id):
    tour = Tournament.objects.get(id=tour_id)
    if tour.started == True:
        rounds = Round.objects.all().filter(tournament=tour)
        context = {'rnds':rounds}
        return render(request, 'tournament/fixtures.html', context)
    
    else:
        form = RequestForm(request.POST)
#        participant = tour.participants
#       count = registered.participant_title.__len__
        if request.method == 'POST':
            if form.is_valid():           
                form.save()
                return redirect('tourlist')
        context = {'tournament':tour, 'form': form}
        return render(request, 'tournament/pretour.html', context)
    
def tourdetail(request, tour_id):
    tour = Tournament.objects.get(id=tour_id)
    requests = Request.objects.all().filter(tournament=tour).order_by('-created')
    waiting = Request.objects.all().filter(tournament=tour,checked=False).count()
    rounds = Round.objects.all().filter(tournament=tour)
    context = {'tour':tour, 'requests':requests,'waiting':waiting, 'rounds':rounds}
    return render(request, 'forstaff/tourdetail.html', context)


def createround(request, tour_id):
    tour = Tournament.objects.get(id=tour_id)
    form = RoundCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            newform = form.save(commit=False)
            newform.tournament = tour
            newform.save()
    
    context = {'form':newform}
    return render(request, 'forstaff/createround.html', context)


class ApprovalRequest(LoginRequiredMixin,generic.UpdateView):
    model = Request
    form_class = ApprovalRequestForm
    success_url = reverse_lazy('advancedtourlist')
    template_name = 'forstaff/approval.html'

    def get_queryset(self):
        return super().get_queryset()
    
#request = form.save(commit=False)
                #request.player = request.user
  #              request.tournament = tour.tournament_name


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
#    return render(request, 'tournament/fixtures.html')""


def roundview(request, rnd_id):
    forround = Round.objects.get(id=rnd_id)
    matches = Match.objects.all().filter(forround=forround)
    context = {'myround':forround, 'matches':matches}
    return render(request, 'tournament/roundview.html', context)
