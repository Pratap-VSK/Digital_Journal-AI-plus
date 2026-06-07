from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.ModelForm):
    class meta:
        model = JournalEntry
        fields = ['title', 'content']