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
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have been logged in successfully!")
            return redirect("journal:dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "account/login.html", {"form": form})

def logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('account:login')
        messages.success(request, "You have been logged out successfully!")
    return render(request, "account/logout.html")

def forgot_password(request):
    return render(request, 'accounts/forgot_password.html')