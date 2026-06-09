import json
import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import CustomRegisterForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard') # Agar logged in hai toh register pe mat aane do
        
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('dashboard')
    else:
        form = CustomRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard') # Agar logged in hai toh direct dashboard
        
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been securely logged out.")
    return redirect('home')

@login_required(login_url='login')
def profile_view(request):
    return render(request, 'account/use_profile.html')

def forgot_password_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            action = data.get('action')

            # STEP A: Email mila, OTP generate karke terminal aur real inbox mein bhejo
            if action == 'send_otp':
                email = data.get('email')
                user = User.objects.filter(email=email).first()
                
                if user:
                    # 6 digit random OTP generate kiya
                    otp = str(random.randint(100000, 999999))
                    request.session['reset_otp'] = otp
                    request.session['reset_email'] = email
                    
                    # 1. Terminal mein print (Testing ke liye fast check)
                    print(f"\n{'='*40}\n🔒 SECURITY OTP FOR {email}: {otp}\n{'='*40}\n")

                    # 2. Real Email Send Logic (Gmail SMTP ke through)
                    subject = 'ProJournal - Password Reset Verification Code'
                    message = f'''Hello {user.username},

We received a request to reset your password for your ProJournal account. 
Here is your 6-digit security OTP code:

{otp}

Please enter this code on the reset page to proceed. If you did not request this, you can safely ignore this email.

Stay Secure,
ProJournal Team'''
                    
                    try:
                        send_mail(
                            subject,
                            message,
                            settings.EMAIL_HOST_USER,  # Sender email accounts se uthayega
                            [email],                   # Target user ki email
                            fail_silently=False,
                        )
                    except Exception as email_err:
                        print(f"SMTP Error: Real email nahi bheja ja saka: {email_err}")
                
                # Security Best Practice: Success hamesha True bhejte hain 
                # taaki koi baar-baar alag emails daal kar registered users ka pata na laga sake
                return JsonResponse({'success': True})

            # STEP B: User ka entered OTP check karo
            elif action == 'verify_otp':
                user_otp = data.get('otp')
                real_otp = request.session.get('reset_otp')
                
                if real_otp and str(user_otp) == str(real_otp):
                    request.session['otp_verified'] = True
                    return JsonResponse({'success': True})
                return JsonResponse({'success': False, 'message': 'Invalid OTP. Please check and try again.'})

            # STEP C: Otp verification
            elif action == 'reset_password':
                if request.session.get('otp_verified'):
                    email = request.session.get('reset_email')
                    new_password = data.get('password')
                    
                    user = User.objects.filter(email=email).first()
                    if user:
                        user.set_password(new_password)
                        user.save()
                
                        request.session.flush()
                        return JsonResponse({'success': True})
                return JsonResponse({'success': False, 'message': 'Session expired or invalid process. Please restart.'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return render(request, 'accounts/forgot_password.html')

def user_profile_views(request):
    return render(request, 'accounts/user_profile.html')