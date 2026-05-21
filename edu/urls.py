from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"api/autores", views.AutorViewSet)
router.register(r"api/editoras", views.EditoraViewSet)

urlpatterns = [
    path("autores/", views.listar_autores, name="listar_autores"),
    path("autores/novo/", views.criar_autor, name="criar_autor"),
    path("autores/editar/<int:id>/", views.editar_autor, name="editar_autor"),
    path("autores/excluir/<int:id>/", views.excluir_autor, name="excluir_autor"),

    path("livros/", views.listar_livros, name="listar_livros"),
    path("livros/novo/", views.criar_livro, name="criar_livro"),
    path("livros/editar/<int:id>/", views.editar_livro, name="editar_livro"),
    path("livros/excluir/<int:id>/", views.excluir_livro, name="excluir_livro"),

    path("cadastro/", views.cadastro_usuario, name="cadastro_usuario"),
    path("login/", views.login_usuario, name="login_usuario"),
    path("logout/", views.logout_usuario, name="logout_usuario"),
    
    
]

urlpatterns += router.urls 