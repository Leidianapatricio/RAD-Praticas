from django.urls import path
from . import views

urlpatterns = [
    path('autores/', views.listar_autores, name='listar_autores'),
    path('autores/novo/', views.criar_autor, name='criar_autor'),
    path('autores/editar/<int:id>/', views.editar_autor, name='editar_autor'),
    path('autores/excluir/<int:id>/', views.excluir_autor, name='excluir_autor'),
]