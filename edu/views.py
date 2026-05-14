from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm
from django.core.paginator import Paginator
from .models import Livro


def listar_autores(request):
    autores = Autor.objects.all()
    return render(request, 'edu/listar_autores.html', {'autores': autores})


def criar_autor(request):
    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_autores')

    return render(request, 'edu/form_autor.html', {'form': form})


def editar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)

    form = AutorForm(request.POST or None, instance=autor)

    if form.is_valid():
        form.save()
        return redirect('listar_autores')

    return render(request, 'edu/form_autor.html', {'form': form})


def excluir_autor(request, id):
    autor = get_object_or_404(Autor, id=id)

    if request.method == 'POST':
        autor.delete()
        return redirect('listar_autores')

    return render(request, 'edu/excluir_autor.html', {'autor': autor})

def listar_livros(request):
    livros = Livro.objects.all().order_by("id")

    paginator = Paginator(livros, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "edu/listar_livros.html", {"page_obj": page_obj})
