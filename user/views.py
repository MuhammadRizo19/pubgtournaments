from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import EditProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

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
    context = {'profile':profile}
    return render(request, 'profile/profile.html', context)

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
    allusers = User.objects.all()
    context = {'allusers':allusers}
    return render(request, 'forstaff/allusers.html',context)

