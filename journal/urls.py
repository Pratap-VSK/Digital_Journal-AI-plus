from django.urls import path
from . import views

urlpatterns = [
    # Route for the main dashboard displaying all entries
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Route to render the form and create a new journal entry
    path('create/', views.entry_create, name='entry_create'),
    
    # Route to view the full details of a specific entry
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
    
    # Route to edit an existing entry
    path('entry/<int:pk>/edit/', views.entry_update, name='entry_update'),
    
    # Route to delete an entry securely
    path('entry/<int:pk>/delete/', views.entry_delete_v, name='entry_delete'),
]