from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import JournalEntry
from .forms import JournalEntryForm
from .ai_service import generate_ai_content  # Aapka GenAI module

@login_required(login_url='login')
def dashboard_view(request):
    # Logged-in user ki saari entries reverse chronological order (newest first) mein nikalega
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal/dashboard.html', {'entries': entries})

@login_required(login_url='login')
def entry_create_view(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            
            # --- GEMINI AI LIVE HANDSHAKE ---
            # AI engine ko clean prompt pass karenge
            prompt = (
                f"Analyze the following journal entry and provide a single brief emotional tag "
                f"with an emoji (e.g., 🟢 Productive, 🔴 Stressed, 🔵 Calm, 🟡 Happy, 💡 Creative). "
                f"Response must be just the tag. Entry: {entry.content}"
            )
            
            try:
                # .env se fetched API key ke chalte ye background request execute hogi
                ai_mood = generate_ai_content(prompt)
                # Safeguard string limitation
                entry.mood_tag = ai_mood[:50] if ai_mood else "⚪ Neutral"
            except Exception as e:
                # Safe fallback agar network timeout ya key authentication fail ho
                print(f"Gemini API Handshake Error: {e}")
                entry.mood_tag = "⚪ Neutral"
            # --------------------------------
            
            entry.save()
            messages.success(request, "Entry saved and AI analysis complete! 🚀")
            return redirect('dashboard')
        else:
            messages.error(request, "Form validation failed. Please review your input.")
    else:
        form = JournalEntryForm()
        
    return render(request, 'journal/Entry_form.html', {'form': form})

@login_required(login_url='login')
def entry_detail_view(request, pk):
    # Data isolation design: Dusra user kisi aur ki entry dynamic URL badal kar nahi dekh sakta
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    return render(request, 'journal/Entry_details.html', {'entry': entry})

@login_required(login_url='login')
def entry_update_view(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            updated_entry = form.save(commit=False)
            
            # Text update hone par AI sentiment analysis firse trigger hoga
            prompt = (
                f"Analyze the following journal entry and provide a single brief emotional tag "
                f"with an emoji (e.g., 🟢 Productive, 🔴 Stressed, 🔵 Calm, 🟡 Happy). "
                f"Response must be just the tag. Entry: {updated_entry.content}"
            )
            try:
                ai_mood = generate_ai_content(prompt)
                updated_entry.mood_tag = ai_mood[:50] if ai_mood else "⚪ Neutral"
            except Exception:
                pass # Fail hone par database ka purana tag hi maintain rahega
                
            updated_entry.save()
            messages.success(request, "Entry updated successfully!")
            return redirect('entry_detail', pk=pk)
    else:
        form = JournalEntryForm(instance=entry)
        
    return render(request, 'journal/Entry_form.html', {'form': form, 'update': True})

@login_required(login_url='login')
def entry_delete_view(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, "Entry permanently deleted. 🗑️")
        return redirect('dashboard')
    return redirect('entry_detail', pk=pk)