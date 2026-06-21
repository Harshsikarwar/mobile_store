from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import singupForm
# Create your views here.
def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/store/dashboard/")
        else:
            messages.error(request,"invalid password or username")
            return redirect("/account/login/")
    else:
        form = AuthenticationForm()
    return render(request,"account/login.html",{"form":form})

def usersignup(request):
    if request.method == 'POST':
        form = singupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/store/dashboard/")
    else:
        form = singupForm
    return render(request,"account/singup.html",{"form":form})

def userLogout(request):
    logout(request)
    return redirect("/account/login/")
