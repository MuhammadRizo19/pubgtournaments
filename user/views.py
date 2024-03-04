from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile, Point, MinusPoint
from .forms import EditProfile, AddPointForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from base.models import Match

def logoutuser(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
            else:
                user = User.objects.create_user(username=username,email=email, password=password1) 
                user.save()
                Profile.objects.create(user=user)
                messages.info(request, 'Account created successfully')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
    return render(request, 'account/register.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'registration/login.html')

def profiledetail(request, pro_id):
    profile = Profile.objects.get(user=request.user)
    match1 = Match.objects.all().filter(player_2=profile.user).count()
    match2 = Match.objects.all().filter(player_1=profile.user).count()
    totalmatches = match1 + match2
    #wins = Match.objects.all().filter(winner=pro_id).count()
    context = {'profile':profile, 'matches':totalmatches}
    return render(request, 'profile/profile.html', context)


# For allusers page to see users detail
def profileview(request, pr_id):
    profile = Profile.objects.get(id=pr_id)
    context = {'profile':profile}
    return render(request, 'forstaff/profileview.html', context)


"""""
def editprofile(request, pro_id):
    profile = Profile.objects.get(id=pro_id)
    form = EditProfile(request.POST or None, request.FILES or None,instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profiledetail')
    else:
        form = EditProfile(instance=request.user.profile)
    return render(request,'profile/editprofile.html', {'form':form})
"""""
class UpdateProfile(LoginRequiredMixin,generic.UpdateView):
    model = Profile
    template_name = 'profile/editprofile.html'
    form_class = EditProfile
    login_url = 'login'

    def form_valid(self, form):
      self.object = form.save(commit=False)
      self.object.save()
      return redirect ('profile', self.object.pk)
    
def allusers(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request, 'forstaff/allusers.html',context)

""""
def addpoint(request):
    if request.method == 'POST':
        form = AddPointForm(request.POST)
        player1 = Profile.objects.get(user=form.player)
        if form.is_valid():
            myform = form.save(commit=False)
            player1.points = player1.points + myform.points
            player1.save()
            myform.save()

        else:
            form = AddPointForm()
        return render()
"""""

def leadersboard(request):
    allprofiles = Profile.objects.all().order_by('-points')
    own = Profile.objects.get(user=request.user)
    context = {'allprofiles':allprofiles, 'own':own}
    return render(request, 'leadersboards.html',context)

def addpoint(request):
    if request.method == 'POST':
        form = AddPointForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('advanced')
    else:
        form = AddPointForm()
        return render(request, 'forstaff/addpoint.html', {'form':form}) 