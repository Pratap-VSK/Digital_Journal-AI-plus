from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class JournalEntry(models.Model):
    #Link entry to the logged-in user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField()

    #AI will fill this field automatically
    mood_tag = models.CharField(max_length=50, blank=True, null=True)

    #TimeStamps
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"