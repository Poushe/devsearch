from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import profile
from .form import customuserregister

# Create your views here.
def profiles(request):
    profiles=profile.objects.all()
    context={'profiles':profiles}
    return render(request, 'users/profiles.html',context)

def userProfile(request,pk):
    liza=profile.objects.get(id=pk)
    topSkills=liza.skills_set.exclude(description__exact='')
    otherSkills=liza.skills_set.filter(description='')
    context={'liza':liza, 'topSkills':topSkills, 'otherSkills':otherSkills}
    return render(request, 'users/user-profile.html',context)

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'Username or Password incorrect')
    return render(request, 'users/login_register.html')
def logoutUser(request):
    logout(request)
    messages.error(request,'User Logout')
    return redirect('login')

def registerUser(request):
    form=customuserregister()
    page='register'
    if request.method=='POST':
        form = customuserregister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'user account created')
            login(request,user)
            return redirect('profiles')
        else:
            messages.success(request, 'An error occured during registration')
    context={'page':page, 'form':form}
    return render(request,'users/login_register.html',context)