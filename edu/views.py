from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import Autor, Livro
from .forms import AutorForm, LivroForm
from .forms_auth import CadastroUsuarioForm


def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, "edu/listar_autores.html", {"autores": autores})


def criar_autor(request):
    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listar_autores")

    return render(request, "edu/form_autor.html", {"form": form})


def editar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    form = AutorForm(request.POST or None, instance=autor)

    if form.is_valid():
        form.save()
        return redirect("listar_autores")

    return render(request, "edu/form_autor.html", {"form": form})


def excluir_autor(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == "POST":
        autor.delete()
        return redirect("listar_autores")

    return render(request, "edu/excluir_autor.html", {"autor": autor})


def listar_livros(request):
    livros = Livro.objects.all().order_by("id")

    paginator = Paginator(livros, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "edu/listar_livros.html", {"page_obj": page_obj})


@login_required
def criar_livro(request):
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("listar_livros")

    return render(request, "edu/form_livro.html", {"form": form})


@login_required
def editar_livro(request, id):
    livro = get_object_or_404(Livro, id=id)
    form = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect("listar_livros")

    return render(request, "edu/form_livro.html", {"form": form})


def cadastro_usuario(request):
    form = CadastroUsuarioForm(request.POST or None)

    if form.is_valid():
        usuario = form.save()
        login(request, usuario)
        return redirect("listar_livros")

    return render(request, "edu/cadastro.html", {"form": form})


def login_usuario(request):
    form = AuthenticationForm(request, data=request.POST or None)

    form.fields["username"].widget.attrs.update({
        "class": "w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
    })

    form.fields["password"].widget.attrs.update({
        "class": "w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
    })

    if form.is_valid():
        usuario = form.get_user()
        login(request, usuario)
        return redirect("listar_livros")

    return render(request, "edu/login.html", {"form": form})


def logout_usuario(request):
    logout(request)
    return redirect("login_usuario")