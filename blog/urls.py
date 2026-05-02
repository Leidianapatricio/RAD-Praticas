from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contato/<str:telefone>/", views.contato, name="contato"),
]

