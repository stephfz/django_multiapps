from django.urls import path, include
from apps.firstApp import views

urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('show_user', views.show_user),
]