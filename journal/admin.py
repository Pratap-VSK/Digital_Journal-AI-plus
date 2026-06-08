from django.contrib import admin
from .models import JournalEntry
# Register your models here.

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'mood_tag', 'created_at')

    search_field = ('title', 'content', 'user__username')
    list_filter = ('mood_tag', 'created_at')
    ordering = ('-created_at',)