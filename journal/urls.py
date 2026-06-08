from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create/', views.entry_create_view, name='entry_create'),
    path('entry/<int:pk>/', views.entry_detail_view, name='entry_detail'),
    path('entry/<int:pk>/update/', views.entry_update_view, name='entry_update'),
    path('entry/<int:pk>/delete/', views.entry_delete_view, name='entry_delete'),
]