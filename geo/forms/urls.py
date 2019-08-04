from django.urls import path, include
from . import views

urlpatterns = [
    path('trial/', views.trial, name='trial'),
]
