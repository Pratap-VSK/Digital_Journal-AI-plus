from django.shortcuts import render, redirect
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, 
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy

# View to handle new user registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        # Render empty form for GET requests
        form = UserCreationForm()
        
    return render(request, 'accounts/register.html', {'form': form})

# --- Custom Subclassed Authentication Views ---
# This keeps the urls.py file clean and allows for easy future logic additions

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True  # Prevents logged-in users from seeing the login page

class CustomLogoutView(LogoutView):
    next_page = 'login'  # Redirects to login page after logging out

class CustomPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    # Uses reverse_lazy to delay URL resolution until the module is fully loaded
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'