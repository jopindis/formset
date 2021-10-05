from django.urls import path
from .import views

urlpatterns = [
    path('home/<str:pk>/', views.home, name="home"),
]
