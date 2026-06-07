from django.urls import path
from . import views

urlpatterns = [
    # Route for the main dashboard displaying all entries
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.entry_create, name='entry_create'),
    path('entry/<int:pk>/', views.entry_detail, name='entry_detail'),
    path('entry/<int:pk>/update/', views.entry_update, name='entry_update'),
    path('entry/<int:pk>/delete/', views.entry_delete, name='entry_delete'),
]