from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have been registered successfully!")
            return redirect("account:login")
    else:
        form = UserCreationForm()
    return render(request, "account/register.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            messages.success(request, "You have been logged in successfully!")
            return redirect("account:dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "account/login.html", {"form": form})

def logout(request):
    messages.success(request, "You have been logged out successfully!")
    return render(request, "account/logout.html")

