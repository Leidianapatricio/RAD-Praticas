from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor
from .forms import AutorForm


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
