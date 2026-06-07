from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import JournalEntry
from .forms import JournalEntryForm

@login_required(login_url='login')
def dashboard(request):
    # Fetch only the logged-in user's entries
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal/dashboard.html', {'entries': entries})

@login_required(login_url='login')
def entry_create(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            # AI Logic will be added here later
            entry.save()
            return redirect('dashboard')
    else:
        form = JournalEntryForm()
        
    return render(request, 'journal/Entry_form.html', {'form': form})

@login_required(login_url='login')
def entry_detail(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    return render(request, 'journal/Entry_details.html', {'entry': entry})

@login_required(login_url='login')
def entry_update(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = JournalEntryForm(instance=entry)
        
    return render(request, 'journal/Entry_form.html', {'form': form, 'update': True})

@login_required(login_url='login')
def entry_delete(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('dashboard')
        
    # Redirect back to details if accessed via GET (Safety measure)
    return redirect('entry_detail', pk=pk)