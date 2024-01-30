from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import EditProfile

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

def editprofile(request, pro_id):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfile(instance=profile, data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    else:
        form = EditProfile(instance=request.user.profile)
    return render(request,'profile/editprofile.html', {'form':form})
