from django import forms
from .models import JournalEntry

class JournalEntryForm(forms.modelsForm):
    class meta:
        model = JournalEntry
        fields = ['title', 'content']